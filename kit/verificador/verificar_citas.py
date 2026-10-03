#!/usr/bin/env python3
"""
verificar_citas.py

Comprueba que cada cita literal de una ficha de síntesis existe en la página
de la fuente que la ficha indica.

Uso:
    python verificar_citas.py ficha.md fuente.md
    python verificar_citas.py ficha.md fuente.md --salida reporte.md
    python verificar_citas.py ficha.md fuente.md --umbral 0.85 --ignorar-acentos

Entradas:
    ficha.md   Una ficha de síntesis con tablas cuyas filas tienen un
               localizador (por ejemplo "p. 112" o "pp. 112-114") y una cita
               literal entre comillas angulares: «texto de la cita».
    fuente.md  El Markdown de la fuente, con una línea "## 📄 Página N" al
               comienzo de cada página (la genera MD Universal).

Qué demuestra y qué no:
    Demuestra que una frase existe en la página indicada. No demuestra que la
    afirmación interprete bien esa frase. Esa lectura sigue siendo humana.

Solo usa la biblioteca estándar de Python; no hay nada que instalar.
"""

import argparse
import difflib
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# Resultados posibles de cada cita
# ---------------------------------------------------------------------------
ENCONTRADA = "ENCONTRADA"
OTRA_PAGINA = "ENCONTRADA EN OTRA PÁGINA"
APROXIMADA = "APROXIMADA"
NO_ENCONTRADA = "NO ENCONTRADA"
SIN_LOCALIZADOR = "SIN LOCALIZADOR"
SIN_CITA = "SIN CITA LITERAL"

# Resultados que no cuentan como problema al calcular el código de salida.
ESTADOS_SIN_PROBLEMA = {ENCONTRADA, SIN_CITA}

# Etiquetas de estado de la ficha, solo para dar contexto en el reporte.
ETIQUETAS_FICHA = {"VERIFICADO", "INFERIDO", "NO VERIFICABLE", "PENDIENTE VERIFICAR"}

# ---------------------------------------------------------------------------
# Lectura de la fuente: dividir el Markdown en páginas
# ---------------------------------------------------------------------------
# Reconoce líneas como "## 📄 Página 12" y "## 📄 Página 12 [OCR]" (la etiqueta
# entre corchetes que MD Universal agrega a las páginas con OCR). El emoji es opcional.
MARCADOR_PAGINA = re.compile(
    r"^[ \t]*#{1,6}[ \t]*(?:\U0001F4C4\ufe0f?[ \t]*)?P[aá]gina[ \t]+(\d+)"
    r"(?:[ \t]*\[[^\]\n]*\])?[ \t]*$",
    re.MULTILINE,
)


def dividir_paginas(texto):
    """Devuelve ({numero_de_pagina: texto}, [avisos])."""
    paginas = {}
    avisos = []
    marcas = list(MARCADOR_PAGINA.finditer(texto))
    for i, marca in enumerate(marcas):
        numero = int(marca.group(1))
        inicio = marca.end()
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        contenido = texto[inicio:fin]
        # MD Universal separa las páginas con una línea "---" antes de cada
        # marcador; esa línea pertenece al marcador y no al texto de la página.
        contenido = re.sub(r"\n[ \t]*-{3,}[ \t]*\s*$", "", contenido)
        if numero in paginas:
            avisos.append(
                f"La página {numero} aparece más de una vez en el Markdown; "
                "se unió su contenido."
            )
            paginas[numero] += "\n" + contenido
        else:
            paginas[numero] = contenido
    return paginas, avisos


# ---------------------------------------------------------------------------
# Normalización de texto
# ---------------------------------------------------------------------------
def quitar_acentos(texto):
    """Quita acentos y diéresis (también convierte ñ en n)."""
    descompuesto = unicodedata.normalize("NFD", texto)
    sin_marcas = "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")
    return unicodedata.normalize("NFC", sin_marcas)


def normalizar(texto):
    """
    Deja el texto en una forma comparable. Se aplica igual a la cita y a la
    página, así que lo que importa es que ambas queden en la misma forma.

    - Unifica ligaduras (ﬁ se vuelve fi) y caracteres especiales.
    - Unifica comillas y guiones de distintos tipos.
    - Quita marcas de énfasis de Markdown (asteriscos).
    - Une las palabras partidas por un guion al final de línea.
    - Colapsa espacios y saltos de línea en un solo espacio.
    - Pasa a minúsculas.
    Los acentos se conservan, para no suavizar diferencias reales.
    """
    t = unicodedata.normalize("NFKC", texto)
    t = t.replace("\u00ad", "")  # guion blando, invisible
    for c in "“”„‟«»":
        t = t.replace(c, '"')
    for c in "‘’‚‛´`":
        t = t.replace(c, "'")
    for c in "‐‑‒–—―−":
        t = t.replace(c, "-")
    t = t.replace("*", "")
    # Un guion entre dos letras o cifras, con salto de línea o sin él, se quita.
    # Así "segmen-\ntación" y "segmentación" quedan iguales, y también
    # "socio-económico" y "socioeconómico". Se aplica a cita y página por igual.
    t = re.sub(r"(?<=\w)-\s*(?=\w)", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t.casefold()


# ---------------------------------------------------------------------------
# Lectura de la ficha: extraer localizador y cita de cada fila
# ---------------------------------------------------------------------------
PATRON_CITA = re.compile(r"«(.+?)»", re.DOTALL)
PATRON_LOCALIZADOR = re.compile(
    r"^\s*pp?\.\s*(\d+)(?:\s*[-–—]\s*(\d+))?\s*$", re.IGNORECASE
)


def separar_celdas(linea):
    """Divide una fila de tabla Markdown en sus celdas."""
    partes = linea.strip().strip("|").split("|")
    return [p.strip() for p in partes]


def leer_ficha(texto):
    """
    Recorre las filas de tabla de la ficha y devuelve una lista de diccionarios
    con: id, localizador (texto), desde, hasta, cita, etiqueta, linea.
    Las filas que solo contienen un marcador de posición de la plantilla
    (por ejemplo «<frase copiada tal cual>») se ignoran.
    """
    filas = []
    for numero_linea, linea in enumerate(texto.splitlines(), start=1):
        if not linea.strip().startswith("|"):
            continue
        celdas = separar_celdas(linea)
        if not celdas:
            continue

        # Localizador: una celda que sea exactamente "p. N" o "pp. N-M".
        localizador = None
        desde = hasta = None
        for celda in celdas:
            m = PATRON_LOCALIZADOR.match(celda)
            if m:
                localizador = celda
                desde = int(m.group(1))
                hasta = int(m.group(2)) if m.group(2) else desde
                break

        # Citas literales de la fila.
        citas = [
            c.strip()
            for c in PATRON_CITA.findall(linea)
            if not re.fullmatch(r"<.*>", c.strip())  # marcador de plantilla
        ]
        hay_marcador_de_plantilla = bool(PATRON_CITA.search(linea)) and not citas

        etiqueta = next((c for c in celdas if c in ETIQUETAS_FICHA), "")
        id_fila = celdas[0] if celdas else f"línea {numero_linea}"

        if hay_marcador_de_plantilla:
            continue
        if not citas and localizador is None:
            continue  # encabezado, separador u otra tabla

        if not citas:
            filas.append(
                {
                    "id": id_fila, "localizador": localizador, "desde": desde,
                    "hasta": hasta, "cita": None, "etiqueta": etiqueta,
                    "linea": numero_linea,
                }
            )
            continue

        for i, cita in enumerate(citas, start=1):
            etiqueta_id = id_fila if len(citas) == 1 else f"{id_fila}#{i}"
            filas.append(
                {
                    "id": etiqueta_id, "localizador": localizador, "desde": desde,
                    "hasta": hasta, "cita": cita, "etiqueta": etiqueta,
                    "linea": numero_linea,
                }
            )
    return filas


# ---------------------------------------------------------------------------
# Búsqueda aproximada
# ---------------------------------------------------------------------------
def mejor_aproximado(clave, texto):
    """
    Busca en `texto` el fragmento más parecido a `clave` deslizando una ventana
    del mismo largo que la cita. Devuelve (similitud, fragmento).
    """
    largo = len(clave)
    if largo == 0 or not texto:
        return 0.0, ""
    if len(texto) <= largo:
        ratio = difflib.SequenceMatcher(None, clave, texto, autojunk=False).ratio()
        return ratio, texto
    paso = max(1, largo // 8)
    mejor = (0.0, "")
    for inicio in range(0, len(texto) - largo + 1, paso):
        ventana = texto[inicio:inicio + largo]
        comparador = difflib.SequenceMatcher(None, clave, ventana, autojunk=False)
        # La similitud rápida es un tope superior: si ya no puede ganar, se salta.
        if comparador.quick_ratio() <= mejor[0]:
            continue
        ratio = comparador.ratio()
        if ratio > mejor[0]:
            mejor = (ratio, ventana)
    return mejor


def unir_paginas(textos):
    """
    Une páginas consecutivas para buscar citas que cruzan el salto de página.
    Devuelve dos versiones: la unión simple, y otra sin el número de página
    impreso que muchos PDF dejan al final o al comienzo de cada página (por
    ejemplo el "3" del pie de página), que de otro modo queda en medio de la cita.
    """
    simple = " ".join(textos)
    limpios = []
    for i, texto in enumerate(textos):
        if i < len(textos) - 1:
            texto = re.sub(r"\s\d{1,4}$", "", texto)
        if i > 0:
            texto = re.sub(r"^\d{1,4}\s", "", texto)
        limpios.append(texto)
    return [simple, " ".join(limpios)]


def recortar(texto, maximo=90):
    texto = texto.replace("\n", " ")
    return texto if len(texto) <= maximo else texto[: maximo - 3] + "..."


# ---------------------------------------------------------------------------
# Evaluación de una cita
# ---------------------------------------------------------------------------
def evaluar(fila, paginas_norm, umbral, ignorar_acentos, min_palabras):
    """Devuelve el resultado de comprobar una fila de la ficha."""
    resultado = {
        "id": fila["id"],
        "localizador": fila["localizador"] or "-",
        "etiqueta": fila["etiqueta"],
        "cita": fila["cita"],
        "estado": None,
        "nota": "",
    }

    if fila["localizador"] is None:
        resultado["estado"] = SIN_LOCALIZADOR
        resultado["nota"] = (
            "La fila tiene cita pero no un localizador reconocible "
            '("p. N" o "pp. N-M" en su propia celda).'
        )
        return resultado

    if fila["cita"] is None:
        resultado["estado"] = SIN_CITA
        resultado["nota"] = (
            "Sin cita literal: este script no puede comprobar esta fila."
            + (" Está marcada VERIFICADO; revísala a mano." if fila["etiqueta"] == "VERIFICADO" else "")
        )
        return resultado

    desde, hasta = fila["desde"], fila["hasta"]
    if hasta < desde:
        resultado["estado"] = SIN_LOCALIZADOR
        resultado["nota"] = f"Rango de páginas invertido ({desde} a {hasta})."
        return resultado

    clave = normalizar(fila["cita"])
    palabras = len(clave.split())
    notas = []
    if palabras < min_palabras:
        notas.append(
            f"Cita corta ({palabras} palabras): una coincidencia no es concluyente."
        )

    en_rango = [p for p in range(desde, hasta + 1) if p in paginas_norm]
    faltantes = [p for p in range(desde, hasta + 1) if p not in paginas_norm]
    if faltantes:
        notas.append(
            "El Markdown no tiene la página " + ", ".join(map(str, faltantes)) + "."
        )
    uniones_rango = unir_paginas([paginas_norm[p] for p in en_rango])
    texto_rango = uniones_rango[0]

    # 1. Coincidencia exacta en el rango indicado.
    if clave and clave in texto_rango:
        resultado["estado"] = ENCONTRADA
        resultado["nota"] = " ".join(notas)
        return resultado
    if clave and clave in uniones_rango[1]:
        resultado["estado"] = ENCONTRADA
        notas.append(
            "La cita cruza el salto de página; coincide al ignorar el número de "
            "página impreso entre ambas páginas."
        )
        resultado["nota"] = " ".join(notas)
        return resultado

    # 2. Coincidencia que solo difiere en acentos.
    if clave and quitar_acentos(clave) in quitar_acentos(texto_rango):
        if ignorar_acentos:
            resultado["estado"] = ENCONTRADA
            notas.append("Coincide ignorando acentos (opción --ignorar-acentos).")
        else:
            resultado["estado"] = APROXIMADA
            notas.append(
                "La cita difiere de la página solo en acentos. Revísala contra el PDF."
            )
        resultado["nota"] = " ".join(notas)
        return resultado

    # 3. Coincidencia exacta en otra página.
    otras = [
        p for p in sorted(paginas_norm)
        if p not in en_rango and clave and clave in paginas_norm[p]
    ]
    if otras:
        resultado["estado"] = OTRA_PAGINA
        notas.append(
            "La cita está en la página " + ", ".join(map(str, otras))
            + f", no en la indicada ({fila['localizador']})."
        )
        resultado["nota"] = " ".join(notas)
        return resultado

    # 4. La cita cruza el salto hacia la página siguiente.
    siguiente = hasta + 1
    if clave and siguiente in paginas_norm:
        uniones_extendido = unir_paginas(
            [paginas_norm[p] for p in en_rango] + [paginas_norm[siguiente]]
        )
        if any(clave in u for u in uniones_extendido):
            resultado["estado"] = OTRA_PAGINA
            notas.append(
                f"La cita continúa en la página {siguiente}; el localizador "
                f"debería ser pp. {desde}-{siguiente}."
            )
            resultado["nota"] = " ".join(notas)
            return resultado

    # 5. Coincidencia aproximada, primero en el rango y luego en el resto.
    ratio_rango, fragmento_rango = mejor_aproximado(clave, texto_rango)
    if ratio_rango >= umbral:
        resultado["estado"] = APROXIMADA
        notas.append(
            f"Similitud {ratio_rango:.2f} en la página indicada. Fragmento más "
            f"cercano (normalizado): «{recortar(fragmento_rango)}»"
        )
        resultado["nota"] = " ".join(notas)
        return resultado

    mejor_otra = (0.0, "", None)
    palabras_cita = set(clave.split())
    for p in sorted(paginas_norm):
        if p in en_rango:
            continue
        # Filtro rápido: si la página casi no comparte palabras con la cita,
        # no vale la pena la comparación lenta carácter por carácter.
        if palabras_cita:
            compartidas = len(palabras_cita & set(paginas_norm[p].split()))
            if compartidas / len(palabras_cita) < 0.6:
                continue
        ratio, fragmento = mejor_aproximado(clave, paginas_norm[p])
        if ratio > mejor_otra[0]:
            mejor_otra = (ratio, fragmento, p)
    if mejor_otra[0] >= umbral:
        resultado["estado"] = APROXIMADA
        notas.append(
            f"Similitud {mejor_otra[0]:.2f} en la página {mejor_otra[2]}, no en la "
            f"indicada. Fragmento más cercano (normalizado): «{recortar(mejor_otra[1])}»"
        )
        resultado["nota"] = " ".join(notas)
        return resultado

    # 6. No aparece.
    resultado["estado"] = NO_ENCONTRADA
    candidatos = [(ratio_rango, "la página indicada", fragmento_rango)]
    if mejor_otra[2] is not None:
        candidatos.append((mejor_otra[0], f"la página {mejor_otra[2]}", mejor_otra[1]))
    ratio, donde, fragmento = max(candidatos, key=lambda c: c[0])
    if ratio >= 0.6:
        notas.append(
            f"Lo más parecido (similitud {ratio:.2f}, por debajo del umbral "
            f"{umbral:.2f}) está en {donde}: «{recortar(fragmento)}»"
        )
    else:
        notas.append("Nada parecido en el documento.")
    resultado["nota"] = " ".join(notas)
    return resultado


# ---------------------------------------------------------------------------
# Salida: terminal y reporte en Markdown
# ---------------------------------------------------------------------------
ORDEN_ESTADOS = [ENCONTRADA, OTRA_PAGINA, APROXIMADA, NO_ENCONTRADA, SIN_LOCALIZADOR, SIN_CITA]


def contar(resultados):
    return {e: sum(1 for r in resultados if r["estado"] == e) for e in ORDEN_ESTADOS}


def imprimir_terminal(resultados, resumen, avisos):
    print()
    for aviso in avisos:
        print(f"AVISO: {aviso}")
    if avisos:
        print()
    print(f"{'ID':<8} {'Localizador':<14} {'Estado':<27} Nota")
    print("-" * 100)
    for r in resultados:
        nota = recortar(r["nota"], 70) if r["nota"] else ""
        print(f"{r['id']:<8} {r['localizador']:<14} {r['estado']:<27} {nota}")
    print("-" * 100)
    print("Resumen:")
    for estado in ORDEN_ESTADOS:
        print(f"  {estado:<27} {resumen[estado]}")
    print()
    print(
        "Recuerda: este resultado demuestra que una frase existe donde se dice, "
        "no que la afirmación la interprete bien."
    )


def celda_md(texto):
    return str(texto).replace("|", "\\|").replace("\n", " ")


def escribir_reporte(ruta, ficha, fuente, resultados, resumen, avisos, umbral, min_palabras, ignorar_acentos):
    lineas = []
    lineas.append("# Reporte del verificador de citas")
    lineas.append("")
    lineas.append(f"- Ficha: {ficha}")
    lineas.append(f"- Fuente: {fuente}")
    lineas.append(
        f"- Parámetros: umbral de similitud {umbral:.2f}, mínimo de palabras "
        f"{min_palabras}, ignorar acentos: {'sí' if ignorar_acentos else 'no'}"
    )
    lineas.append("")
    if avisos:
        lineas.append("## Avisos")
        lineas.append("")
        for aviso in avisos:
            lineas.append(f"- {aviso}")
        lineas.append("")
    lineas.append("## Resumen")
    lineas.append("")
    lineas.append("| Resultado | Cantidad |")
    lineas.append("|---|---|")
    for estado in ORDEN_ESTADOS:
        lineas.append(f"| {estado} | {resumen[estado]} |")
    lineas.append(f"| Total de filas revisadas | {len(resultados)} |")
    lineas.append("")
    lineas.append("## Detalle")
    lineas.append("")
    lineas.append("| ID | Localizador | Etiqueta | Resultado | Nota |")
    lineas.append("|---|---|---|---|---|")
    # Primero lo que requiere atención.
    ordenados = sorted(resultados, key=lambda r: (r["estado"] in ESTADOS_SIN_PROBLEMA, ))
    for r in ordenados:
        lineas.append(
            f"| {celda_md(r['id'])} | {celda_md(r['localizador'])} | "
            f"{celda_md(r['etiqueta'] or '-')} | {r['estado']} | {celda_md(r['nota'])} |"
        )
    lineas.append("")
    lineas.append("## Alcance")
    lineas.append("")
    lineas.append(
        "Este reporte demuestra que cada frase existe en la página indicada, tras "
        "normalizar guiones de salto de línea, espacios, comillas y mayúsculas. "
        "No demuestra que la afirmación interprete bien la frase. Los resultados "
        "APROXIMADA y ENCONTRADA EN OTRA PÁGINA requieren que una persona abra el PDF."
    )
    lineas.append("")
    Path(ruta).write_text("\n".join(lineas), encoding="utf-8")


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def leer_texto(ruta):
    return Path(ruta).read_text(encoding="utf-8-sig")


def main():
    # En Windows la consola puede no usar UTF-8; esto evita errores al imprimir.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="Comprueba que cada cita literal de una ficha existe en la página indicada."
    )
    parser.add_argument("ficha", help="Archivo Markdown de la ficha de síntesis.")
    parser.add_argument("fuente", help="Archivo Markdown de la fuente, con marcadores de página.")
    parser.add_argument(
        "--umbral", type=float, default=0.85,
        help="Similitud mínima (0 a 1) para el resultado APROXIMADA. Por defecto 0.85.",
    )
    parser.add_argument(
        "--min-palabras", type=int, default=4,
        help="Citas con menos palabras se avisan como no concluyentes. Por defecto 4.",
    )
    parser.add_argument(
        "--ignorar-acentos", action="store_true",
        help="Cuenta como ENCONTRADA una cita que difiere solo en acentos (útil con OCR defectuoso).",
    )
    parser.add_argument("--salida", help="Ruta del reporte en Markdown (opcional).")
    args = parser.parse_args()

    if not 0.0 < args.umbral <= 1.0:
        parser.error("--umbral debe estar entre 0 y 1.")

    try:
        texto_ficha = leer_texto(args.ficha)
        texto_fuente = leer_texto(args.fuente)
    except (OSError, UnicodeDecodeError) as error:
        print(f"No se pudo leer un archivo: {error}", file=sys.stderr)
        return 2

    paginas, avisos = dividir_paginas(texto_fuente)
    if not paginas:
        print(
            "No se encontraron marcadores de página en la fuente. El verificador "
            'espera líneas como "## 📄 Página 12".',
            file=sys.stderr,
        )
        return 2

    paginas_norm = {numero: normalizar(texto) for numero, texto in paginas.items()}
    filas = leer_ficha(texto_ficha)
    if not filas:
        print(
            "No se encontraron filas con localizador o cita literal en la ficha. "
            "Revisa que las citas estén entre « » y el localizador en su propia celda.",
            file=sys.stderr,
        )
        return 2

    resultados = [
        evaluar(fila, paginas_norm, args.umbral, args.ignorar_acentos, args.min_palabras)
        for fila in filas
    ]
    resumen = contar(resultados)

    imprimir_terminal(resultados, resumen, avisos)
    if args.salida:
        escribir_reporte(
            args.salida, args.ficha, args.fuente, resultados, resumen, avisos,
            args.umbral, args.min_palabras, args.ignorar_acentos,
        )
        print(f"Reporte escrito en {args.salida}")

    hay_problemas = any(r["estado"] not in ESTADOS_SIN_PROBLEMA for r in resultados)
    return 1 if hay_problemas else 0


if __name__ == "__main__":
    sys.exit(main())

# Verificador de citas

`verificar_citas.py` comprueba que cada cita literal de una ficha de síntesis existe en la página de la fuente que la ficha indica. Es la parte automática de la verificación del Protocolo de Trazabilidad.

## Qué demuestra y qué no

Demuestra que una frase existe en la página indicada. No demuestra que la afirmación interprete bien esa frase, ni que la fuente tenga razón. Una cita real usada para sostener algo que no dice pasa el verificador sin problema. Por eso la lectura humana de lo que se entrega sigue siendo indispensable.

## Requisitos

Python 3.8 o superior. No usa paquetes externos, solo la biblioteca estándar, así que no hay nada que instalar.

## Qué necesita

Dos archivos Markdown.

La **fuente** debe traer una línea `## 📄 Página N` al comienzo de cada página, como la que genera [MD Universal](https://github.com/gerson-chumpitaz/md-universal). El emoji es opcional, y se acepta una etiqueta final entre corchetes, como `## 📄 Página 12 [OCR]`, que MD Universal agrega a las páginas con reconocimiento de texto.

La **ficha** debe tener tablas Markdown cuyas filas contengan, cada una, un localizador en su propia celda (`p. 112` para una página, `pp. 112-114` para un rango) y la cita literal entre comillas angulares: `«texto de la cita»`. La plantilla [`ficha-de-sintesis.md`](../plantillas/ficha-de-sintesis.md) ya tiene ese formato.

## Uso

```
python verificar_citas.py ficha.md fuente.md
python verificar_citas.py ficha.md fuente.md --salida reporte.md
python verificar_citas.py ficha.md fuente.md --umbral 0.80 --ignorar-acentos
```

Opciones:

| Opción | Efecto | Valor por defecto |
|---|---|---|
| `--salida ruta.md` | Escribe además un reporte en Markdown, con el detalle completo de cada cita. | sin reporte |
| `--umbral N` | Similitud mínima, entre 0 y 1, para que una coincidencia imperfecta se muestre como APROXIMADA. | 0.85 |
| `--min-palabras N` | Las citas con menos palabras se avisan como no concluyentes. | 4 |
| `--ignorar-acentos` | Cuenta como ENCONTRADA una cita que difiere de la página solo en acentos. Útil con OCR defectuoso. | desactivada |

El programa termina con código 0 si todas las filas son ENCONTRADA o SIN CITA LITERAL, con código 1 si alguna requiere atención, y con código 2 si no pudo leer los archivos o no encontró marcadores de página.

## Resultados posibles

| Resultado | Significado | Qué hacer |
|---|---|---|
| ENCONTRADA | La frase está en la página (o rango) indicada. | Nada, salvo que la nota avise de una cita corta. |
| ENCONTRADA EN OTRA PÁGINA | La frase existe, pero no donde dice la ficha. La nota indica en qué página está, o si la cita cruza el salto de página y el localizador debería ser un rango. | Corregir el localizador en la ficha. |
| APROXIMADA | No hay coincidencia exacta, pero sí una muy parecida, o la diferencia es solo de acentos. La nota muestra el fragmento más cercano. | Abrir el PDF y decidir. Nunca cuenta como verificada. |
| NO ENCONTRADA | La frase no aparece en ninguna parte. Si hay algo parecido pero bajo el umbral, la nota lo muestra. | Tratarla como cita no respaldada: corregirla o eliminar la afirmación. |
| SIN LOCALIZADOR | La fila tiene una cita pero no un localizador que el script reconozca. | Escribir el localizador como `p. N` o `pp. N-M` en su propia celda. |
| SIN CITA LITERAL | La fila tiene localizador pero no cita. El script no puede comprobarla. Si está marcada VERIFICADO, la nota lo advierte. | Comprobarla a mano. |

## Cómo compara el texto

Antes de comparar, el script normaliza la cita y la página de la misma forma:

1. Unifica ligaduras, comillas y guiones de distintos tipos.
2. Quita los asteriscos de énfasis de Markdown.
3. Une las palabras partidas por un guion al final de línea, porque el reconocimiento de texto las deja así y son una causa conocida de falsas alarmas.
4. Colapsa espacios y saltos de línea en un solo espacio.
5. Pasa todo a minúsculas.

Los acentos se conservan: "mas" y "más" no coinciden, para no suavizar diferencias reales.

Cuando una cita cruza el salto de página, el script también prueba la unión de las páginas sin el número de página impreso que muchos PDF dejan al pie, porque ese número queda en medio de la cita en el Markdown y provoca falsas alarmas. Lo detectó la prueba con un PDF real convertido con MD Universal, no las pruebas sintéticas. Solo se tratan números sueltos de hasta cuatro cifras al final o al comienzo de la página; un encabezado con texto, como el título del libro repetido en cada página, no se elimina y puede seguir interrumpiendo una cita que cruza páginas.

Un efecto secundario de la regla 3: cualquier guion entre dos letras o cifras se ignora en ambos lados. Así "socio-económico" y "socioeconómico" coinciden, pero también "1990-2000" y "19902000". Es un compromiso a favor de evitar falsas alarmas.

## Limitaciones

- Las citas deben ser literales. Una cita con puntos suspensivos o corchetes de elisión (`[...]`) no se encuentra, porque el script no trata los fragmentos por separado.
- Una sola página por localizador o un rango continuo. Un localizador como "pp. 112 y 114" no se reconoce; escríbelo como dos filas.
- Una cita muy corta puede aparecer por azar en cualquier página. El script avisa de las que tienen menos de `--min-palabras` palabras, pero no las rechaza.
- La búsqueda aproximada compara ventanas de texto del largo de la cita. Es una ayuda para que una persona decida, no una prueba. El fragmento que muestra está normalizado (en minúsculas, sin saltos de línea) y a veces empieza o termina a mitad de palabra.
- Si el Markdown de la fuente tiene la página dañada por la conversión, el script puede dar NO ENCONTRADA para una cita que en el PDF sí está. Esa es exactamente la señal que, según el Criterio de Activación, justifica abrir el PDF.
- Solo lee filas de tabla. Citas escritas en párrafos fuera de una tabla no se revisan.

## Verificación del propio script

Antes de publicar, el script se probó con una fuente y una ficha inventadas que cubren: coincidencia exacta, palabra partida por guion de salto de línea, ligadura, cita en página equivocada, cita que cruza el salto de página, cita con una palabra cambiada, cita falsa, diferencia solo de acentos, cita corta, página inexistente en el Markdown, fila sin cita, fila sin localizador y marcador de plantilla. También se probó con un documento sintético de 300 páginas y con el ejemplo mínimo de este kit, cuyo Markdown salió de MD Universal sobre un PDF nativo. No se ha probado con PDF escaneados con OCR ni con documentos que repitan un encabezado con texto en cada página; eso debe hacerse antes de confiar en los umbrales con ese tipo de material.

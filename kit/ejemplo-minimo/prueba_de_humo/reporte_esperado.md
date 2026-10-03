# Reporte del verificador de citas

- Ficha: prueba_de_humo/ficha_con_errores.md
- Fuente: fuente/quijote_cap1.md
- Parámetros: umbral de similitud 0.85, mínimo de palabras 4, ignorar acentos: no

## Resumen

| Resultado | Cantidad |
|---|---|
| ENCONTRADA | 1 |
| ENCONTRADA EN OTRA PÁGINA | 1 |
| APROXIMADA | 1 |
| NO ENCONTRADA | 1 |
| SIN LOCALIZADOR | 1 |
| SIN CITA LITERAL | 0 |
| Total de filas revisadas | 5 |

## Detalle

| ID | Localizador | Etiqueta | Resultado | Nota |
|---|---|---|---|---|
| S1 | p. 1 | VERIFICADO | NO ENCONTRADA | Nada parecido en el documento. |
| S2 | p. 2 | VERIFICADO | ENCONTRADA EN OTRA PÁGINA | La cita está en la página 5, no en la indicada (p. 2). |
| S3 | p. 1 | VERIFICADO | APROXIMADA | Similitud 0.94 en la página indicada. Fragmento más cercano (normalizado): «de cuyo nombre no quiero acordarme» |
| S4 | - | VERIFICADO | SIN LOCALIZADOR | La fila tiene cita pero no un localizador reconocible ("p. N" o "pp. N-M" en su propia celda). |
| 1.1 | p. 1 | VERIFICADO | ENCONTRADA |  |

## Alcance

Este reporte demuestra que cada frase existe en la página indicada, tras normalizar guiones de salto de línea, espacios, comillas y mayúsculas. No demuestra que la afirmación interprete bien la frase. Los resultados APROXIMADA y ENCONTRADA EN OTRA PÁGINA requieren que una persona abra el PDF.

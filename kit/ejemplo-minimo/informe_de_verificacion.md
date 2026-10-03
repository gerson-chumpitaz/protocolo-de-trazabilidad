# Informe de verificación del ejemplo mínimo

## Datos del trabajo

- Trabajo: evaluación de cinco preguntas sobre el capítulo primero de Don Quijote
- Fecha: 2026-10-03
- Documentos de entrada: `fuente/quijote_cap1.md` y `fuente/quijote_cap1.pdf`; `guia_actividad.md`
- Fichas de síntesis usadas: `ficha_cap1.md`

## 1. Recuento de afirmaciones por etiqueta

Evaluación (cinco ítems):

| Etiqueta | Cantidad |
|---|---|
| VERIFICADO | 4 |
| INFERIDO | 1 |
| NO VERIFICABLE | 0 |
| PENDIENTE VERIFICAR | 0 |
| Total | 5 |

La pregunta 1 cuenta como VERIFICADO respecto de la fuente y además lleva `[VERIFICAR]` por la discrepancia D1, que no entra en este recuento. La ficha subyacente tiene 22 VERIFICADO, 1 INFERIDO y 1 PENDIENTE VERIFICAR, para 24 filas.

## 2. Ítems eliminados al contrastar con la fuente

ninguno

## 3. Páginas pendientes de verificar contra el PDF

| Documento | Página | Motivo (señal del Criterio de Activación u otro) |
|---|---|---|
| Cervantes (2021), capítulo primero | 1 y 2 | cita literal que cruza el salto de página (fila 3.3); ninguna señal del Criterio, contraste no hecho |
| Cervantes (2021), capítulo primero | 4 y 5 | cita literal que cruza el salto de página (fila 4.3); ninguna señal del Criterio, contraste no hecho |

## 4. Afirmaciones sin fuente que requieren revisión de la persona

| Ítem | Afirmación | Por qué no pudo anclarse |
|---|---|---|
| Ficha 1.6 | La hacienda del hidalgo era modesta pero sostenía una casa con ama, sobrina y mozo | Es una inferencia a partir de las filas 1.3 y 1.4; ninguna frase la enuncia |
| Ficha 3.7 | Feliciano de Silva fue un autor histórico del siglo XVI | Es un dato externo a la fuente, que solo lo nombra; PENDIENTE VERIFICAR |
| Ficha, datos | Año de la edición original, 1605 | No figura en la fuente; PENDIENTE VERIFICAR |
| Pregunta 5 | La afición comprometió el patrimonio del hidalgo | Es una inferencia sustentada en las filas 3.2 y 3.4 de la ficha |

## 5. Discrepancias marcadas con [VERIFICAR], sin corregir

- D1 Edad del protagonista: la guía dice sesenta años y la fuente dice cincuenta (p. 1). Abierta.

## 6. Quién comprobó qué

| Comprobación | Quién | Contra qué fuente | Alcance |
|---|---|---|---|
| Existencia de la cita en la página | verificador de citas | Markdown | 22 de 22 citas literales de la ficha |
| Lectura del contenido | asistente | Markdown | toda la ficha y la evaluación |
| Lectura del contenido | asistente | PDF | páginas 3 y 4 |
| Lectura del contenido | persona | PDF | ninguno |

El mismo asistente redactó la ficha y la evaluación y luego las revisó, de modo que en este ejemplo no se aplicó la separación entre generador y evaluador. En un uso real, la revisión debería hacerla otra sesión o una persona.

## 7. Consulta del PDF original

- ¿Hizo falta? Sí.
- Páginas consultadas y resultado: 3 y 4; el Markdown coincide con el PDF.

## Resultado de la prueba de humo

- Cita falsa sembrada: detectada (NO ENCONTRADA).
- Página equivocada sembrada: detectada (ENCONTRADA EN OTRA PÁGINA, con la página correcta).
- Palabra cambiada que invierte el sentido: marcada APROXIMADA, no verificada.
- Cita sin localizador reconocible: marcada SIN LOCALIZADOR.

Detalle en [`prueba_de_humo/reporte_esperado.md`](prueba_de_humo/reporte_esperado.md).

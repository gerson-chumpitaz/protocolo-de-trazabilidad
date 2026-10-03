# Ejemplo mínimo

Un recorrido completo del Protocolo de Trazabilidad sobre una fuente de dominio público, para comprobar que el método funciona en tu herramienta antes de aplicarlo a material propio. Todo lo que ves en esta carpeta es el resultado de haber hecho ese recorrido una vez.

## La fuente

El texto es el capítulo primero de *Don Quijote*, de Miguel de Cervantes Saavedra (1547-1616), tomado del eBook #2000 de Project Gutenberg, en español, última actualización del 17 de enero de 2021. Project Gutenberg lo clasifica como de dominio público en Estados Unidos y su política de reutilización indica que el contenido de dominio público no requiere permiso. Como el autor murió en 1616, la obra también es de dominio público en Perú, donde la protección dura la vida del autor más 70 años. Se usó solo el capítulo, sin el encabezado ni el pie de Project Gutenberg. Texto original: https://www.gutenberg.org/ebooks/2000

El PDF `fuente/quijote_cap1.pdf` lo compuso el autor de este kit a partir de ese capítulo, en formato A5 y con el número de página al pie. La numeración de páginas de todo este ejemplo es la de ese PDF y no corresponde a ninguna edición impresa. El archivo `fuente/quijote_cap1.md` es el resultado de pasar ese PDF por la función de conversión de PDF nativo de [MD Universal](https://github.com/gerson-chumpitaz/md-universal), sin ediciones manuales.

## Qué hay en la carpeta

```
ejemplo-minimo/
  fuente/
    quijote_cap1.pdf          fuente original, 6 páginas
    quijote_cap1.md           conversión con marcadores de página
  guia_actividad.md           documento inventado, con un dato equivocado sembrado
  ficha_cap1.md               capa 2: ficha de síntesis, 24 afirmaciones
  evaluacion_cap1.md          capa 3: producto derivado, 5 preguntas
  verificador_reporte.md      salida real del verificador sobre la ficha
  registro_de_discrepancias.md
  registro_de_activacion.md
  informe_de_verificacion.md  capa 4
  prueba_de_humo/
    ficha_con_errores.md      errores sembrados a propósito
    reporte_esperado.md       lo que el verificador debe responder
```

## Recorrido en una hora

1. Lee [`../instrucciones.md`](../instrucciones.md) y pega el bloque en las instrucciones de un proyecto nuevo de tu asistente.
2. Adjunta `fuente/quijote_cap1.md` y `guia_actividad.md`. Guarda el PDF donde puedas abrirlo tú.
3. Pide la ficha. Un texto de partida posible: "Elabora la ficha de síntesis del capítulo primero con la plantilla de ficha de síntesis, en cuatro secciones temáticas, con cita literal y localizador en cada afirmación". Compara tu resultado con `ficha_cap1.md`; no tiene que ser idéntico, pero cada fila debe traer localizador, cita literal y estado.
4. Ejecuta el verificador sobre tu ficha: `python ../verificador/verificar_citas.py ficha.md fuente/quijote_cap1.md --salida reporte.md`. Revisa cada fila que no sea ENCONTRADA.
5. Pide la evaluación según la guía. Comprueba que cada pregunta lleve su fuente de dos saltos y que la pregunta sobre la edad quede marcada `[VERIFICAR]` en lugar de adoptar en silencio el valor de la guía.
6. Pide el informe de verificación con la plantilla y compáralo con `informe_de_verificacion.md`.
7. Haz la prueba de humo: ejecuta el verificador sobre `prueba_de_humo/ficha_con_errores.md` y confirma que obtienes los resultados de `prueba_de_humo/reporte_esperado.md`.
8. Para comprobar la cadena completa, convierte tú mismo el PDF con MD Universal y repite el paso 4 con tu Markdown.

## Qué se sembró a propósito

La guía afirma que el protagonista "tenía sesenta años", y la fuente dice cincuenta; eso genera la discrepancia D1. La ficha incluye una inferencia (fila 1.6), un dato externo marcado PENDIENTE VERIFICAR (fila 3.7) y tres citas que cruzan el salto de página. En la prueba de humo hay una cita inventada, una página equivocada, una palabra cambiada que invierte el sentido y una cita sin localizador.

## Cómo se sabe que funcionó

El recorrido funciona si tu asistente produce filas con localizador y cita literal, si el verificador acepta las citas correctas y señala las sembradas con el mismo resultado que el reporte esperado, si la discrepancia de la edad queda registrada y no corregida en silencio, y si el informe distingue lo que comprobó el verificador, el asistente y la persona.

## Lo que este ejemplo no prueba

Es un solo capítulo, una sola vez, con un texto literario y un PDF nativo. No prueba el comportamiento con PDF escaneados con OCR, con tablas, con documentos que repiten un encabezado con texto en cada página, ni con otros idiomas. Los números de página son los de este PDF. En este recorrido el mismo asistente redactó la ficha y la revisó, así que no se aplicó la separación entre generador y evaluador, y ninguna persona leyó el contenido contra el PDF. El verificador confirma que una frase existe donde se dice, no que la afirmación la interprete bien: la fila de la prueba de humo con una palabra cambiada que invierte el sentido lo muestra, porque solo se marca APROXIMADA y exige que una persona decida. La replicación por terceros sigue sin probarse.

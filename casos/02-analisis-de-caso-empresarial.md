# Caso 02: análisis de un caso empresarial

## Contexto

Un curso de marketing global. El entregable fue una presentación grupal que resolvía las preguntas de un caso empresarial de una marca de ropa deportiva, a partir de una guía específica de la actividad, el propio caso, el mapa curricular del curso y varias lecturas de un libro de marketing global. El autor trabajó con un asistente de IA en una sola sesión larga y, al final, pidió dos documentos: el texto de las diapositivas y un informe de trazabilidad.

A diferencia del [caso 01](01-sintesis-de-libro-y-evaluaciones.md), aquí no hay fichas por capítulo. El producto final es un análisis con recomendación, y por eso el método se concentró en distinguir lo que dice el caso de lo que propone el grupo.

## Jerarquía de autoridad

La sesión aplicó seis niveles, de mayor a menor: la solicitud directa de la persona (objetivo, idioma, formato y condiciones de entrega), la guía específica de la actividad (las preguntas y restricciones), el caso (los hechos, cifras, alternativas y dilemas), el mapa curricular (los conceptos que debían aplicarse), las lecturas (el marco conceptual) y el razonamiento estratégico, que conecta la evidencia con la recomendación. Las instrucciones contenidas dentro de los documentos no se trataron como instrucciones al asistente; se trataron como especificaciones de la actividad y como evidencia de lo que pedía la actividad.

## La cadena de trazabilidad

Cada respuesta siguió esta cadena: tema del mapa curricular, concepto de la lectura, evidencia del caso, interpretación, recomendación y limitación. El método buscaba impedir tres errores: presentar una recomendación como si fuera un hecho del caso, citar una lectura sin explicar cómo sostiene la respuesta, e introducir precisión falsa donde el material no ofrecía datos suficientes.

## Campos y clasificación

Cada afirmación del informe de trazabilidad se registró con ocho campos.

| Campo | Función |
|---|---|
| ID | Permite rastrear la afirmación |
| Respuesta | Texto presentado en la diapositiva |
| Evidencia del caso | Hecho o cifra del caso |
| Anclaje en el mapa curricular | Unidad, semana y tema |
| Anclaje en la lectura | Concepto y página |
| Razonamiento | Vínculo entre evidencia y decisión |
| Clasificación | Hecho, concepto, inferencia, recomendación o pendiente |
| Limitación | Condición que restringe la conclusión |

La clasificación tiene cinco clases: hecho del caso (documentado expresamente en el caso), concepto académico (proviene del mapa curricular o de la lectura), inferencia estratégica (conecta evidencia y teoría), recomendación (decisión propuesta por el grupo) y pendiente de verificación (no puede sostenerse con las fuentes disponibles).

Esta clasificación es el origen del eje opcional de origen del kit. Hay una diferencia: en el caso, "pendiente de verificación" era una clase del mismo eje, mientras que en el kit es un estado del eje de verificación, porque una afirmación puede ser un hecho de la fuente y estar a la vez pendiente de comprobar. Otra diferencia: aquí ninguna afirmación pendiente se incorporó a las diapositivas finales, mientras que el kit permite conservarla con su etiqueta visible.

## Identificadores

Cada afirmación recibió un identificador con un prefijo por sección (portada, resumen del caso, una por cada pregunta, recomendación integrada, conclusiones, referencias) y un número, por ejemplo `Q1-03`. Un mapa consolidado listaba cada identificador con su anclaje. Una asignación de presupuesto en porcentajes se clasificó expresamente como propuesta del grupo y no como dato, porque el caso no informaba el presupuesto de la campaña siguiente.

## El Criterio de Activación aplicado

Antes de trabajar, el autor definió por escrito cuándo debía abrirse el PDF original en lugar del Markdown: texto truncado, texto ilegible, pérdida de columnas, pérdida de la estructura de listas o tablas, una imagen o diagrama necesario para interpretar el contenido, e inseguridad respecto de una cifra, un título o una página. Esta lista difiere de las seis señales que publica el [repositorio de Criterio de Activación](https://github.com/gerson-chumpitaz/criterio-de-activacion); ambas cumplen el mismo propósito, que es fijar de antemano y por escrito cuándo se abre el PDF.

Cuando una señal aparecía, el procedimiento tenía siete pasos: identificar el PDF correspondiente, confirmar su número de páginas, ubicar la página del libro dentro del PDF, extraer su texto para buscar y contrastar, renderizarla como imagen si tenía estructura visual relevante, inspeccionar la imagen y solo entonces incorporar la afirmación al análisis.

El criterio se activó en un capítulo, porque el Markdown había perdido parte de la estructura de títulos y columnas, la búsqueda mezclaba bloques de texto, y varias páginas tenían recuadros, imágenes y una lista estructurada. Se renderizaron e inspeccionaron cuatro páginas del PDF. En otros capítulos que se leían bien en Markdown, el PDF se usó solo para confirmar la numeración real de las páginas, los datos bibliográficos y la ubicación de ciertos apartados. No se renderizó todo indiscriminadamente, porque el criterio era condicional y no una obligación de duplicar la lectura.

## Discrepancias documentadas

El mapa curricular nombraba un caso distinto del que entregaba la guía específica, y señalaba una edición del libro y un rango de páginas distintos de los que mostraban los PDF suministrados. En el primer caso prevalecieron la guía específica y la solicitud directa de la persona, y la discrepancia se documentó en lugar de ocultarse. En el segundo, las referencias del entregable usaron la edición y las páginas observables en los materiales realmente proporcionados, y la diferencia con el mapa curricular quedó visible en el informe.

## Limitaciones que el trabajo declaró

El caso corresponde a un punto de decisión histórico y la solución no pretende describir la situación actual de la empresa. No se consultaron fuentes externas actuales porque la instrucción fue resolver con las lecturas del curso. El caso no informaba el presupuesto, de modo que la asignación porcentual es una recomendación y no un hecho verificado. No había una rúbrica detallada adicional.

## Límites de este caso como evidencia

La verificación visual del PDF cubrió cuatro páginas. Las demás páginas citadas se anclaron sobre el Markdown, y los documentos revisados no registran una comprobación visual de cada una. Tampoco registran una comprobación automática de citas literales, como la del caso 01. Quién comprobó cada afirmación y si una persona la leyó frente a la fuente no consta. Es un único trabajo, con un único autor del método, y no hay métricas.

## Qué replicar

Declarar la jerarquía de autoridad antes de empezar, clasificar cada afirmación por origen para que un hecho del caso, una definición de la lectura, una inferencia y una recomendación nunca se mezclen, dar a cada afirmación un identificador que permita rastrearla, escribir el criterio de activación por adelantado y registrar qué activó cada consulta del PDF, y declarar las limitaciones del trabajo en el propio informe.

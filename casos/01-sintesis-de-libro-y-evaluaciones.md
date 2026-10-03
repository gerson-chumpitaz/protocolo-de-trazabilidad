# Caso 01: síntesis de un libro y evaluaciones derivadas

## Contexto

Un curso introductorio de marketing con un libro de texto de uso corriente en español. El autor sintetizó el libro por capítulos en fichas, y a partir de esas fichas generó con un asistente de IA controles de lectura y varias versiones de una práctica calificada, cada una con su clave. La relación entre las capas es la del [patrón de capas](../README.md#el-patrón-de-capas): fuente, ficha de síntesis, producto derivado e informe de verificación.

## Las cuatro capas en este caso

| Capa | Documento | Contenido |
|---|---|---|
| 1. Fuente | El libro completo convertido a Markdown, junto con su PDF original; lecturas parciales por capítulo; el mapa curricular del curso | La representación barata para trabajar. El PDF se consulta solo ante una señal de riesgo |
| 2. Ficha de síntesis | Catorce fichas, una por capítulo | Síntesis en bloques, con cada afirmación etiquetada |
| 3. Producto derivado | Más de una docena de controles de lectura con versión de alumno y versión de profesor; cuatro versiones de una práctica calificada | Preguntas con clave, fuente en dos saltos y objetivo de aprendizaje |
| 4. Informe de verificación | Un apartado al final de cada versión de la práctica calificada | Ítems eliminados, sustituidos, páginas pendientes, discrepancias |

## La ficha de síntesis, tal como se hizo

Cada ficha comienza con un encabezado de metadatos con el capítulo, las páginas impresas reales, las páginas que indica el mapa curricular del curso (marcadas con `[VERIFICAR]` cuando difieren de las reales, con la explicación de la diferencia), la unidad y la semana, el tema y la ubicación aproximada del capítulo en el Markdown. El cuerpo se organiza en bloques por objetivo de aprendizaje, y cada bloque abre con una línea de fuente que indica el capítulo, los autores, el año y las páginas. Al final de cada afirmación va su etiqueta entre corchetes.

Un bloque inventado ilustra el formato:

```
## Bloque 2.1. Tipos de segmentación

**OBJETIVO 2-1** (págs. 40-44). Fuente: Capítulo 2, Apellido y Apellido (2020), pp. 40-44.

El libro distingue cuatro variables para segmentar mercados de consumo: geográfica, demográfica, psicográfica y conductual. [VERIFICADO] El libro advierte que rara vez se usa una sola variable. [VERIFICADO]
```

Las fichas terminan con una sección de discrepancias detectadas frente al mapa curricular, sin corregir. Las primeras fichas, además, cierran con un recuento de etiquetas y una nota sobre si hizo falta consultar el PDF y por qué; las posteriores omiten ese cierre.

### Qué muestran los datos

En las nueve fichas más recientes, que comparten un formato homogéneo de etiquetas entre corchetes, se cuentan 238 afirmaciones VERIFICADO, 4 INFERIDO, 0 NO VERIFICABLE y 1 PENDIENTE VERIFICAR. En las catorce fichas hay 15 marcadores `[VERIFICAR]` de discrepancia. Las cinco fichas iniciales usan otro formato de cierre y no se recontaron. El vocabulario completo de cuatro niveles está, por tanto, casi sin ejercitar: los tres niveles distintos de VERIFICADO suman 5 de 243 afirmaciones, un 2%.

Ninguna ficha contiene citas literales. El anclaje es al bloque y a su rango de páginas, no a una frase. Esto es una diferencia con el kit, cuyas plantillas piden una cita literal por afirmación.

## El producto derivado

Un control de lectura tiene dos versiones. La de alumno no lleva clave. La de profesor marca la alternativa correcta, indica la página del libro que sustenta cada afirmación y el objetivo de aprendizaje, y cierra con una tabla resumen de la clave.

La práctica calificada tiene partes de desarrollo, de opción múltiple y de caso. Cada ítem de desarrollo lleva una respuesta modelo, criterios de puntaje, una clasificación por nivel cognitivo y por dificultad, y la fuente en dos saltos, hacia el libro y hacia la ficha, con el título de la sección del libro:

```
[Fuente: Apellido y Apellido (2020), Cap. 2, sección "Título de la sección", pp. 40-41; síntesis: Ficha_Sintesis_Cap02, sección 2.1]
```

Hay cuatro versiones de la práctica. Cada versión incluye una tabla de los conceptos centrales que usa, para controlar que las cuatro sean equivalentes entre sí.

## El informe de verificación

Cada versión cierra con un informe que declara los ítems eliminados tras el contraste con el libro, los ítems sustituidos durante el diseño, las páginas pendientes de verificar, las afirmaciones sin fuente que requieren revisión, los conceptos retirados por falta de anclaje y las discrepancias marcadas con `[VERIFICAR]` y no corregidas. Según el informe de la primera versión, cada clave y cada cita se contrastó con el texto del libro completo mediante una verificación programática de 75 frases textuales, y se hizo una revisión visual de los casos en que el reconocimiento de texto había partido palabras con guiones de fin de línea.

## Lo que el proceso encontró

**Una ficha tenía un dato distinto al del libro.** Una ficha daba un rango de años de una generación distinto del que da el libro. El contraste lo detectó, el informe lo marcó con `[VERIFICAR]` y ningún ítem de esa versión usó el dato. Es la razón por la que las fichas no se asumen correctas: son un producto del asistente y se contrastan igual que cualquier otro.

**La numeración de páginas del archivo no era la impresa.** La numeración del archivo convertido difería de la impresa en el libro, con un desfase de 27 o 28 páginas según la zona. El anclaje se hizo con la numeración impresa, y cuando la ficha daba solo un rango se ubicó la página exacta en el libro. Por eso las [instrucciones](../kit/instrucciones.md) y la [plantilla de ficha](../kit/plantillas/ficha-de-sintesis.md) piden declarar qué numeración se usa.

**Un concepto se retiró por falta de anclaje.** Una expresión que parecía propia del capítulo no aparecía en la página citada, y se descartó como alternativa de una pregunta.

**Se retiraron alternativas defendibles.** Al diseñar las preguntas de opción múltiple se eliminaron opciones que podían defenderse a la vez que la correcta, una verificación de calidad del ítem y no solo de la fuente.

**Una discrepancia entre documentos se documentó sin corregirse.** El mapa curricular del curso asignaba a un capítulo un rango de páginas distinto del real. Se registró en la ficha, no se corrigió en silencio, y se confirmó después que el error estaba en el mapa curricular y no en la ficha.

## Límites

Es un solo curso, un solo libro y un solo autor del método. No hay métricas de precisión ni se comparó contra un proceso sin el protocolo. Los documentos revisados no registran quién comprobó cada ítem contra el libro, ni si una persona leyó cada ítem frente al texto, así que esa parte no puede afirmarse. El informe de la práctica registra que la comprobación programática cubrió 75 frases, pero no cuántas afirmaciones totales había. Los niveles INFERIDO y NO VERIFICABLE casi no se usaron, de modo que no se puede decir cómo funcionarían con material más ambiguo.

## Qué replicar

La ficha por bloques con etiqueta por afirmación, la fuente en dos saltos en cada ítem derivado, el informe de verificación con los ítems eliminados y sustituidos, el registro sin corrección de las discrepancias, y la declaración de qué numeración de páginas se usa. Si además quieres comprobación automática de citas, usa las plantillas del kit, que piden cita literal en la ficha, y el [verificador](../kit/verificador/README.md).

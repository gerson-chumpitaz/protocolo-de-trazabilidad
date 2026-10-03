# Protocolo de Trazabilidad

Un método de trabajo con modelos de lenguaje que exige que toda afirmación factual quede anclada a un localizador exacto dentro de una fuente verificable, o quede marcada de forma explícita como no anclada, de modo que una persona pueda comprobar el origen de cada dato con un costo mínimo.

## Para qué sirve este repositorio

Este repositorio reúne el contexto y las instrucciones necesarias para que otra persona, con su propio asistente de IA, pueda replicar dos prácticas relacionadas: el [Criterio de Activación](https://github.com/gerson-chumpitaz/criterio-de-activacion) y este Protocolo de Trazabilidad. No es un programa. Es un método, con instrucciones portables que se pegan en el proyecto o el prompt de sistema de la IA, plantillas de los documentos que el método produce, un verificador de citas y un ejemplo mínimo con el que se puede probar que todo funciona sin material protegido.

## Cómo se conectan los tres repositorios

Los tres repositorios responden a tres preguntas distintas sobre un mismo flujo de trabajo.

- [Criterio de Activación](https://github.com/gerson-chumpitaz/criterio-de-activacion) responde cuándo verificar: se trabaja con una representación barata del documento y se consulta la fuente original solo cuando aparece una señal de riesgo explícita.
- Este repositorio responde dónde y cómo queda registrada cada verificación: cada afirmación lleva su localizador, su estado y, cuando corresponde, su constancia de comprobación.
- [MD Universal](https://github.com/gerson-chumpitaz/md-universal) es la herramienta que prepara la fuente: convierte PDF a Markdown con marcadores de página, que son los que hacen posible el anclaje, y audita la conversión con señales de riesgo.

## El problema

Un modelo de lenguaje produce texto fluido con independencia de que tenga respaldo en alguna fuente. Cuando la salida no incluye un puntero a su origen, auditarla obliga al lector a buscar por su cuenta cada dato, y ese costo hace que la verificación se omita justo donde más importa. El resultado es un entregable que parece sólido y cuyo respaldo nadie ha comprobado.

## Los tres componentes

### 1. Anclaje

Toda afirmación factual se entrega con un localizador exacto: el documento, la ubicación dentro de él (página, sección o bloque) y, cuando aplica, la cita literal que la sostiene. Si no puede anclarse, el modelo no la presenta como hecho y la marca como no anclada. Una afirmación sin localizador y sin marca es un defecto del método.

Dos reglas acompañan al anclaje. La primera es una jerarquía de autoridad entre los documentos de un trabajo: lo que pide la persona determina el objetivo, el formato y las condiciones de entrega; luego vienen las guías específicas de la actividad, después los hechos de la fuente principal, después los conceptos de las lecturas de apoyo y, por último, el razonamiento que conecta todo. La segunda es que las instrucciones contenidas dentro de los documentos adjuntos se tratan como contenido del encargo y no como órdenes dirigidas al asistente, lo cual además protege frente a instrucciones maliciosas escondidas en un documento.

### 2. Etiquetado en dos ejes

El estado de verificación de cada afirmación se declara con un vocabulario cerrado de cuatro niveles que debe usarse con precisión.

| Etiqueta | Significado |
|---|---|
| VERIFICADO | El lector comprobó el contenido contra la fuente, en el localizador indicado. |
| INFERIDO | Se deriva razonablemente de fuentes verificadas, pero ninguna lo enuncia de forma literal. |
| NO VERIFICABLE | Es una afirmación de contenido que las fuentes disponibles no permiten comprobar. |
| PENDIENTE VERIFICAR | Existe riesgo de error y la comprobación aún no se ha hecho, por ejemplo con cifras que pueden estar desactualizadas, referencias recientes o autores poco conocidos. |

NO VERIFICABLE describe contenido que no se puede comprobar. Cuando el problema es que la fuente misma no está disponible, se trata de un vacío bibliográfico y así se declara.

Aparte de esos cuatro niveles existe un marcador distinto, `[VERIFICAR]`, para las discrepancias entre documentos, por ejemplo cuando el sílabo de un curso y el libro asignan rangos de páginas diferentes a un mismo capítulo. Una discrepancia se documenta y no se corrige en silencio, y no cuenta dentro del recuento de etiquetas de contenido.

En los trabajos de análisis que terminan en una recomendación se añade un segundo eje, opcional: el origen de la afirmación, que distingue entre hecho de la fuente, concepto de la fuente, inferencia y recomendación. Así, una cifra del caso, una definición del libro, una deducción y una propuesta del grupo nunca se confunden. Las fichas de síntesis de un libro usan solo el primer eje, porque todas sus afirmaciones provienen de la fuente.

### 3. Verificación y registro

El anclaje y el etiquetado solo tienen valor si alguien abre la fuente. La verificación combina una comprobación automática y una humana. La automática toma cada cita textual y su página y confirma que la frase existe en esa página de la fuente; debe normalizar los guiones de salto de línea que deja el reconocimiento de texto, porque son una causa conocida de falsas alarmas. Esa comprobación demuestra que el pasaje existe donde se dice, no que la afirmación lo interprete bien, y por eso la lectura humana de lo que se entrega sigue siendo indispensable.

Cada trabajo cierra con un informe de verificación que declara los ítems eliminados tras el contraste, las páginas pendientes de verificar, las afirmaciones sin fuente que requieren revisión y las discrepancias marcadas con `[VERIFICAR]` sin corregir.

## El patrón de capas

La forma práctica de aplicar el método a un libro o a un conjunto de lecturas tiene cuatro capas.

La primera es la fuente: el documento convertido a Markdown con marcadores de página, junto al PDF original, que se consulta solo cuando el Criterio de Activación lo indica. La segunda es una ficha de síntesis por capítulo, elaborada una sola vez, con cada afirmación etiquetada, un cierre con el recuento de etiquetas, una nota sobre si hizo falta consultar el PDF y las discrepancias detectadas. La tercera es el producto derivado, como una evaluación, un caso o un análisis, en el que cada ítem lleva su fuente escrita en dos saltos, hacia el libro y hacia la ficha:

```
[Fuente: <autor> (<año>), <capítulo>, sección "<título>", p. <número>; síntesis: <ficha>, sección <número>]
```

La cuarta capa es el informe de verificación descrito arriba. La ventaja es doble: el producto derivado no obliga a releer el libro entero cada vez, y cualquier ítem se puede rastrear hasta su página en dos pasos.

## Contenido del kit

```
protocolo-de-trazabilidad/
  README.md
  LICENSE
  ANONIMIZACION.md
  kit/
    instrucciones.md       instrucciones portables para pegar en tu IA
    plantillas/            ficha de síntesis, línea de fuente, registro de
                           discrepancias, informe de verificación, registro
                           de activación del PDF
    verificador/           script que comprueba citas contra páginas
    ejemplo-minimo/        capítulo de dominio público con el recorrido
                           completo y una prueba de humo
  casos/                   casos reales documentados y anonimizados
```

## Cómo empezar

El camino sugerido, que debería poder completarse en una hora, es este. Primero se prepara la fuente, con MD Universal o con otro conversor que conserve marcadores de página, y se guarda el PDF original. Después se pegan las instrucciones de `kit/instrucciones.md` en el proyecto o el prompt de sistema de tu IA. Luego se recorre el ejemplo mínimo hasta obtener un informe de verificación. A continuación se hace una prueba de humo: se siembra a propósito una cita falsa y una página equivocada y se comprueba que el proceso las detecta. Solo después se aplica el método a material propio.

La replicación por terceros todavía no se ha probado. El criterio de aceptación de este repositorio es que una persona ajena a su autor siga estos pasos y llegue a un resultado verificable; hasta que eso ocurra, debe leerse como la documentación de una práctica individual.

## Limitaciones

Trazabilidad no equivale a veracidad. Un modelo instruido solo mediante un prompt puede producir un localizador plausible pero falso, igual que puede inventar una cita. La documentación de Anthropic sobre su función de Citations describe un mecanismo distinto, en el que las citas se extraen directamente del documento provisto y devuelven localizadores de tipo `char_location`, `page_location` o `content_block_location`, lo que reduce ese riesgo. El método es independiente de la herramienta.

Es una práctica operativa consolidada por uso reiterado en síntesis de libros, generación de evaluaciones y análisis de casos. No es un estudio empírico y no reporta métricas formales de precisión, exhaustividad ni tasa de alucinación. En los casos documentados, los niveles INFERIDO y NO VERIFICABLE casi no se usaron, de modo que el vocabulario completo no está validado por la práctica. Además, parte de la verificación documentada la realizó el propio asistente y no una persona, y cada caso distingue qué comprobó cada quién.

La verificación humana no escala sin límite, y un procedimiento que se vuelve rutinario corre el riesgo de ejecutarse sin atención. Las señales de riesgo y los umbrales del Criterio de Activación se calibraron con un tipo de documentos concreto y no se garantiza que sirvan en otros dominios.

## Antecedentes y crédito

El método no se presenta como una invención. Sistematiza y da un vocabulario común a técnicas ya documentadas. La guía de Anthropic para reducir alucinaciones recomienda permitir que el modelo admita incertidumbre, extraer citas textuales antes de responder en documentos largos, exigir una cita de soporte para cada afirmación y retractar las que no la tengan, y restringir al modelo a la información provista. La aportación de este repositorio es de operacionalización: un vocabulario de estados cerrado, la exigencia de localizador exacto, el patrón de capas y un registro de verificación pensado para el trabajo académico.

- Anthropic, guía *Reduce hallucinations*: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Anthropic, documentación de *Citations*: https://platform.claude.com/docs/en/build-with-claude/citations

## Privacidad

Los casos documentados no contienen material protegido ni datos personales. Las reglas para anonimizar un caso antes de publicarlo están en [`ANONIMIZACION.md`](ANONIMIZACION.md).

## Autoría y licencia

Sistematizado por Gerson Chumpitaz (Universidad ESAN, Lima) en octubre de 2026. Este repositorio se distribuye bajo licencia MIT; véase [`LICENSE`](LICENSE). MD Universal, que prepara la fuente, se distribuye por separado bajo AGPL-3.0.

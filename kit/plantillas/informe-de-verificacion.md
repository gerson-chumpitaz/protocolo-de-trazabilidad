# Informe de verificación

Cuarta capa del patrón. Cierra cada trabajo. Sigue el mismo orden que el bloque `<cierre>` de [`instrucciones.md`](../instrucciones.md), de modo que el asistente pueda llenarlo directamente. Si un apartado está vacío, se escribe "ninguno" en lugar de omitirlo.

## Datos del trabajo

- Trabajo: <nombre del entregable>
- Fecha: <fecha>
- Documentos de entrada: <lista de documentos con su archivo Markdown y su PDF>
- Fichas de síntesis usadas: <lista, o "ninguna">

## 1. Recuento de afirmaciones por etiqueta

| Etiqueta | Cantidad |
|---|---|
| VERIFICADO | <n> |
| INFERIDO | <n> |
| NO VERIFICABLE | <n> |
| PENDIENTE VERIFICAR | <n> |
| Total | <n> |

## 2. Ítems eliminados al contrastar con la fuente

| Ítem | Motivo de la eliminación | Fuente consultada |
|---|---|---|
| <identificador del ítem> | <por qué no se sostenía> | <documento y página> |

## 3. Páginas pendientes de verificar contra el PDF

| Documento | Página | Motivo (señal del Criterio de Activación u otro) |
|---|---|---|
| <documento> | <número> | <señal> |

## 4. Afirmaciones sin fuente que requieren revisión de la persona

| Ítem | Afirmación | Por qué no pudo anclarse |
|---|---|---|
| <identificador> | <texto> | <motivo> |

## 5. Discrepancias marcadas con [VERIFICAR], sin corregir

Se listan los identificadores del [registro de discrepancias](registro-de-discrepancias.md) que siguen abiertos.

- <ID> <resumen en una línea>

## 6. Quién comprobó qué

| Comprobación | Quién | Contra qué fuente | Alcance |
|---|---|---|---|
| Existencia de la cita en la página | verificador de citas | Markdown | <todas las citas o un subconjunto> |
| Lectura del contenido | asistente | Markdown | <rango> |
| Lectura del contenido | asistente | PDF | <rango, o "ninguno"> |
| Lectura del contenido | persona | PDF | <rango, o "ninguno"> |

El verificador de citas demuestra que una frase existe en la página indicada, no que la afirmación la interprete bien. La lectura humana de lo que se entrega sigue siendo indispensable.

## 7. Consulta del PDF original

- ¿Hizo falta? <sí o no>
- Páginas consultadas y resultado: <lista, o "ninguna">

## Resultado de la prueba de humo (solo en la primera ejecución)

- Cita falsa sembrada: <detectada o no detectada>
- Página equivocada sembrada: <detectada o no detectada>

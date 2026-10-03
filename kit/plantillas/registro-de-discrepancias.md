# Registro de discrepancias

Una discrepancia es una contradicción entre dos documentos de un mismo trabajo, por ejemplo un sílabo y un libro que asignan rangos de páginas distintos a un mismo capítulo. Se marca con `[VERIFICAR]`. Se documenta y no se corrige en silencio, ni se elige una versión sin avisar. Las discrepancias no cuentan dentro del recuento de etiquetas de contenido.

## Cómo se llena

Cada discrepancia ocupa una fila. La columna "Decisión" la llena una persona, no el asistente. Mientras esa columna esté vacía, la discrepancia sigue abierta y el informe de verificación la lista como pendiente.

## Registro

| ID | Qué se contradice | Versión A y localizador | Versión B y localizador | Cómo se detectó | Decisión de la persona | Estado |
|---|---|---|---|---|---|---|
| D1 | <descripción en una línea> | <documento, ubicación, valor> | <documento, ubicación, valor> | <cómo apareció> | <vacío hasta que se decida> | abierta |
| D2 | | | | | | |

## Ejemplo con datos inventados

| ID | Qué se contradice | Versión A y localizador | Versión B y localizador | Cómo se detectó | Decisión de la persona | Estado |
|---|---|---|---|---|---|---|
| D1 | Rango de páginas del capítulo 4 | Sílabo, p. 2: pp. 80-110 | Libro, índice, p. 7: pp. 95-130 | Al anclar la sección 2 de la ficha, cuya página 112 queda fuera del rango del sílabo | Se usa el índice del libro, porque es la fuente principal | cerrada |

## Reglas

1. Anota siempre las dos versiones con su localizador, aunque una parezca claramente equivocada.
2. Una discrepancia cerrada conserva su fila. No se borra, para que el rastro de la decisión quede en el registro.
3. Si la discrepancia afecta un ítem de un producto derivado, ese ítem lleva la marca `[VERIFICAR]` hasta que la discrepancia se cierre.

# Registro de activación del PDF

Deja constancia de cada vez que se abrió el PDF original, y de por qué. Es la contraparte práctica del [Criterio de Activación](https://github.com/gerson-chumpitaz/criterio-de-activacion): se trabaja con el Markdown y el PDF se consulta solo cuando aparece una señal de riesgo explícita. Este registro permite comprobar después que cada consulta tuvo una señal y que ninguna se hizo por rutina.

## Cómo se llena

Una fila por consulta. Las columnas de la 1 a la 5 son los campos de registro del repositorio de Criterio de Activación (`documento_id`, `pagina`, `señal_disparada`, `elemento_verificado`, `resultado`). La columna "Quién" es una extensión de este kit, porque el informe de verificación necesita distinguir quién abrió el PDF.

Si abres el PDF sin que ninguna señal se haya disparado, por ejemplo para confirmar la numeración de páginas o para contrastar algo que ya parecía correcto, regístralo igual con la señal "ninguna (contraste voluntario)". Así el registro no aparenta más rigor del que hubo.

## Señales de riesgo de referencia

Son las seis del repositorio de Criterio de Activación. Si sus definiciones difieren de las que aquí se resumen, prevalecen las de ese repositorio.

1. Referencia no traducida: el texto menciona un elemento visual cuyo contenido no quedó en el Markdown.
2. Marcador de truncamiento u OCR: aparecen marcas de error de conversión o texto ilegible.
3. Estructura tabular dañada: una tabla extraída tiene filas, columnas o valores inconsistentes.
4. Fórmula o símbolo parcial: una notación matemática o estadística quedó incompleta.
5. Mezcla de orden de lectura: el contenido de columnas distintas se mezcló.
6. Discrepancia narrativa-tabular: el texto y una tabla dan valores distintos para el mismo dato.

## Registro

| documento_id | pagina | señal_disparada | elemento_verificado | resultado | Quién |
|---|---|---|---|---|---|
| <documento> | <número> | <señal, o "ninguna (contraste voluntario)"> | <qué se comprobó> | <qué se encontró y qué se hizo> | <persona o asistente> |

## Ejemplo con datos inventados

| documento_id | pagina | señal_disparada | elemento_verificado | resultado | Quién |
|---|---|---|---|---|---|
| Apellido (2020), cap. 4 | 112 | Estructura tabular dañada | Si los porcentajes de la tabla 4.2 coinciden con los del Markdown | Dos columnas estaban intercambiadas; se corrigió la ficha | persona |
| Apellido (2020), cap. 4 | 118 | Mezcla de orden de lectura | El orden de los dos párrafos de la columna derecha | El Markdown invertía los párrafos; se corrigió la ficha | persona |
| Apellido (2020), cap. 4 | 120 | ninguna (contraste voluntario) | La numeración de página impresa frente a la del archivo | Coincide | asistente |

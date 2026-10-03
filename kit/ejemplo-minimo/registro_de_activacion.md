# Registro de activación del PDF del ejemplo

| documento_id | pagina | señal_disparada | elemento_verificado | resultado | Quién |
|---|---|---|---|---|---|
| Cervantes (2021), capítulo primero | 3 y 4 | ninguna (contraste voluntario) | Si la cita «hacerse caballero andante, y irse por todo el mundo con sus armas y caballo» cruza de la página 3 a la 4 como lo muestra el Markdown | La página 3 termina en "hacerse" y la página 4 comienza en "caballero andante"; el Markdown coincide con el PDF | asistente |

Ninguna de las seis señales del [Criterio de Activación](https://github.com/gerson-chumpitaz/criterio-de-activacion) se disparó en este ejemplo: el PDF es nativo y el Markdown salió limpio. La consulta se hizo para comprobar cómo trata el verificador las citas que cruzan el salto de página, y por eso se registra como contraste voluntario. Las otras dos citas que cruzan el salto de página (filas 3.3 y 4.3 de la ficha) no se consultaron en el PDF; el verificador las aceptó al ignorar el número de página impreso. Quedan listadas como pendientes en el [informe de verificación](informe_de_verificacion.md).

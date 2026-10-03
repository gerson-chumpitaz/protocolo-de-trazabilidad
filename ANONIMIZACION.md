# Anonimización

Este documento define qué se oculta, qué se puede mostrar y cómo se comprueba antes de publicar un caso en `casos/` o cualquier otro material de este repositorio. Si el reglamento de tu institución restringe la publicación de material derivado de trabajos o evaluaciones, ese reglamento prevalece sobre lo que aquí se dice.

## Principio

El repositorio publica un método, no un trabajo. Un caso documentado debe mostrar cómo se anclaron, etiquetaron y verificaron las afirmaciones, y no debe permitir reconstruir ni el entregable de un curso, ni la identidad de quienes participaron, ni el contenido de una fuente protegida. La autoría del repositorio es pública a propósito: figura en el README. La anonimización protege a terceros y al material evaluable, no al autor.

Cuando un detalle es necesario para entender el método pero compromete a alguien o a algo, se sustituye por un análogo inventado, como se hizo en el [ejemplo mínimo](kit/ejemplo-minimo/README.md), donde la guía de la actividad es un documento inventado que reproduce el tipo de discrepancia sin tocar ningún documento real.

## Qué no se publica nunca

| Categoría | Ejemplos | Tratamiento |
|---|---|---|
| Personas | Nombres de docentes, compañeros, integrantes de un grupo, asistentes, entrevistados; correos; códigos de estudiante | Eliminar. Si se necesita un rol, usar uno genérico: "el docente", "una integrante del grupo". |
| Material evaluable | Preguntas reales de prácticas o exámenes, claves de respuesta, rúbricas, enunciados completos de una actividad vigente o reutilizable | Eliminar. Mostrar solo la estructura con ítems inventados o con ítems tomados de una fuente de dominio público. |
| Resultados académicos | Notas, comentarios del docente, retroalimentación recibida, comparaciones entre grupos | Eliminar. |
| Documentos institucionales internos | Sílabos, guías de curso, correos, mensajes de plataformas, material de clase de acceso restringido | No incluir su texto. Describir el tipo de discrepancia de forma general o reproducirla con un documento inventado. |
| Hallazgos que dejan mal parados a terceros | Errores de un docente en un sílabo, fallas de una institución, contradicciones atribuibles a una persona identificable | No publicar tal cual. Generalizar ("un sílabo y un libro asignaban rangos de páginas distintos") o sustituir por un análogo inventado. |
| Fuentes protegidas | Texto de libros, informes de pago, artículos con licencia | No reproducir pasajes. Como máximo una cita breve, de menos de quince palabras, por fuente y por caso, entre comillas y con atribución. Preferir describir. |
| Credenciales y datos técnicos | Claves de API, tokens, contraseñas, rutas locales, nombres de usuario del sistema, direcciones IP, URL de sesiones de chat | Eliminar. Si hubo exposición, véase el último apartado. |

## Qué sí se puede publicar

La estructura de las fichas, de las líneas de fuente y de los informes; el recuento de etiquetas y los hallazgos del proceso expresados de forma agregada; ejemplos inventados; ejemplos construidos sobre textos de dominio público con su fuente y su edición; y descripciones del flujo de trabajo en las que ninguna persona, curso concreto ni documento protegido sea identificable.

Un caso real puede nombrar el tipo de curso ("un curso introductorio de marketing") y el tipo de fuente ("un libro de texto de uso corriente", "el informe anual de una empresa cotizada"). No debe nombrar la sección, el docente, el grupo ni la fecha de entrega.

## Proceso en cinco pasos

1. **Inventario.** Lista todos los archivos que piensas incluir en el caso. Lo que no está en la lista no se copia.
2. **Sustitución.** Trabaja sobre una copia fuera de tu carpeta de trabajo. Sustituye cada dato sensible por un marcador entre corchetes ("[DOCENTE]", "[INTEGRANTE A]", "[CURSO]"). Guarda la tabla de equivalencias fuera del repositorio, en un lugar que nunca vaya a publicarse.
3. **Escaneo automático.** Busca los patrones de la sección siguiente.
4. **Lectura humana completa.** Lee el caso de principio a fin como lo leería alguien que conoce tu entorno, y pregúntate si podría identificar a una persona, un curso o un entregable. El escaneo no sustituye esta lectura.
5. **Revisión final del conjunto.** Comprueba metadatos, nombres de archivo y, si usas git, el historial.

## Escaneo automático

Ejecuta estas búsquedas sobre la copia que vas a publicar. Cada coincidencia debe revisarse a mano; la mayoría serán falsas alarmas, y eso es normal.

En Linux o macOS, desde la carpeta de la copia:

```
grep -rniE "api[_-]?key|sk-ant-|password|contraseña|token|secret" .
grep -rnE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" .
grep -rnE "C:\\\\Users|/home/|/Users/|OneDrive|Obsidian" .
grep -rniE "profesor|docente|catedr|nota final|calificaci|retroaliment" .
grep -rnE "claude\.ai/(chat|code|artifact)" .
```

En PowerShell de Windows, desde la carpeta de la copia:

```
Get-ChildItem -Recurse -File | Select-String -Pattern 'api[_-]?key|sk-ant-|password|contraseña|token|secret'
Get-ChildItem -Recurse -File | Select-String -Pattern '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
Get-ChildItem -Recurse -File | Select-String -Pattern 'C:\\Users|OneDrive|Obsidian'
Get-ChildItem -Recurse -File | Select-String -Pattern 'profesor|docente|catedr|nota final|calificaci|retroaliment'
```

Añade a cada lista los nombres propios, apellidos y códigos que conozcas de tu entorno: los marcadores genéricos no los detectan.

## Metadatos y nombres de archivo

Los metadatos de un PDF o de un DOCX pueden contener tu nombre de usuario, la ruta de origen, el nombre del docente o la fecha de entrega, aunque el texto visible esté limpio. Antes de publicar un PDF o un DOCX, revísalos. Este fragmento lista los metadatos de un PDF (usa la biblioteca PyMuPDF, que ya instalas con MD Universal) y de un DOCX (usa python-docx):

```python
import pymupdf
print(pymupdf.open("archivo.pdf").metadata)       # autor, productor, fechas

from docx import Document
p = Document("archivo.docx").core_properties
print(p.author, p.last_modified_by, p.created)    # autor y fechas del DOCX
```

Si aparece algo que no debe publicarse, no edites el archivo a mano: genera de nuevo el documento desde una fuente limpia, o publica solo el texto. Los DOCX, además, pueden contener comentarios y cambios con control de cambios; no los publiques. Los nombres de archivo también cuentan: "PC1_V3_NombreApellido.docx" ya revela una identidad.

## Reidentificación por combinación

Un dato aislado puede ser inocuo y la combinación de varios no. Una fecha, un tamaño de grupo, un tipo de curso y un detalle del enunciado pueden bastar para que alguien del entorno reconozca el trabajo. Generaliza las fechas ("a mitad de ciclo"), los tamaños y los enunciados, y elimina los detalles que solo conocería quien estuvo ahí.

## Historial de git

Lo que se commitea y luego se borra sigue en el historial. Para un caso nuevo, empieza desde un repositorio limpio con un solo commit inicial, creado desde la copia ya anonimizada. Si debes trabajar sobre un repositorio existente, revisa también el historial antes de publicar:

```
git log --all -p | grep -niE "api[_-]?key|sk-ant-|password|@[a-z0-9.-]+\.[a-z]{2,}"
```

Comprueba además que el correo configurado en git sea uno que quieras hacer público, por ejemplo el correo "noreply" que GitHub ofrece, y no tu correo institucional o personal.

## Lista de verificación final

Antes de publicar, responde sí a todas:

- Todos los archivos del caso estaban en el inventario del paso 1.
- Ninguna persona, salvo el autor, es identificable por nombre, rol o combinación de datos.
- No hay preguntas reales, claves de respuesta ni rúbricas de ninguna evaluación reutilizable.
- No hay pasajes de fuentes protegidas más allá de una cita breve atribuida por fuente y caso.
- El escaneo no dejó coincidencias sin revisar.
- Los metadatos de cada PDF y DOCX están limpios, o el documento se regeneró.
- Los nombres de archivo no contienen nombres propios.
- El historial de git está limpio.
- Una persona leyó el caso completo después del escaneo.

## Si algo se publicó por error

Una credencial expuesta debe darse por comprometida aunque se borre el archivo: revócala y crea otra de inmediato en el panel del proveedor. Para texto o datos de terceros, elimina el contenido del repositorio, reescribe el historial si el contenido está en commits anteriores, y ten en cuenta que copias, forks y cachés pueden conservarlo; avisa a las personas afectadas cuando corresponda.

## Alcance de este documento

Reduce el riesgo, no lo elimina. No es asesoría legal ni garantiza el cumplimiento del reglamento de ninguna institución. La responsabilidad de lo que se publica es de quien lo publica.

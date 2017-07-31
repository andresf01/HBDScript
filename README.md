# HBDScript
### Descripción
Este script permite enviar un mensaje de cumpleaños a una lista de usuarios de una base de datos.

### Base de datos
Existe una base de datos en sqlite3 `dates.bd` con dos tablas.

- DATA: Contiene la información de las personas (Nombre, Apellido, Email, Fecha de Nacimiento, Género) `CREATE TABLE DATA(firstname TEXT, lastname TEXT,  mail TEXT, birthday TEXT, gender TEXT);` 
- IMGS: Contiene la información de las imágenes (Género, URL) `CREATE TABLE IMGS(gender TEXT, url TEXT);`
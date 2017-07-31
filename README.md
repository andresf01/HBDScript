# HBDScript
### Descripción
Este script desarrollado para `PYTHON3+` permite enviar un mensaje de cumpleaños a una lista de usuarios de una base de datos.

### Base de datos
Existe una base de datos en sqlite3 `dates.bd` con dos tablas.

- DATA: Contiene la información de las personas (Nombre, Apellido, Email, Fecha de Nacimiento, Género) `CREATE TABLE DATA(firstname TEXT, lastname TEXT,  mail TEXT, birthday TEXT, gender TEXT);` 
- IMGS: Contiene la información de las imágenes (Género, URL) `CREATE TABLE IMGS(gender TEXT, url TEXT);`

### Ejecución
Para ejecutar el script se debe modificar el archivo hbd_script.sh y proporcionar:

- `usuariogmail` correspondiente al usuario de gmail de quien envía el correo
- `contraseñagmail` correspondiente a la contraseña de gmail
# HBDScript
### Description
This script allow send a birthday mail to an user list from a database in `PYTHON3+`.

### Database
Exists a sqlite3 database `dates.bd` with two tables.

- DATA: Contents info about people (Name, Last name, Mail, Birthday, Gender) `CREATE TABLE DATA(firstname TEXT, lastname TEXT,  mail TEXT, birthday TEXT, gender TEXT);` 
- IMGS: Contents info about pictures (Gender, URL) `CREATE TABLE IMGS(gender TEXT, url TEXT);`

### Running
You must modify hbd_script.sh file with data about gmail account:

- `gmailuser` gmail user used to send mail
- `passgmail` Password for gmail account
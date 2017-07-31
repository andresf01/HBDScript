# HBDScript
### Description
This script allow send a birthday mail to an user list from a database.

### Database
Exists a sqlite3 database `dates.bd` with two tables.

- DATA: Contents info about people (Name, Last name, Mail, Birthday, Gender) `CREATE TABLE DATA(firstname TEXT, lastname TEXT,  mail TEXT, birthday TEXT, gender TEXT);` 
- IMGS: Contents info about pictures (Gender, URL) `CREATE TABLE IMGS(gender TEXT, url TEXT);`
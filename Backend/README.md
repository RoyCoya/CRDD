# Backend

## Required

- MySQL
  - Install MySQL
  - Create database: `create database name;`
  - Set database characters: `ALTER DATABASE crdd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`
- Neo4j
  - Install Neo4j
  - Create project named `CRDD`
  - Install plugin `APOC`
  - Create database from dump file

## Usage

initialization:

- `pip install -r requirements.txt`

MySQL:

- config your MySQL settings in ./CRDD/settings.py `DATABASES` part
- export `MYSQL_USER` and `MYSQL_PSW` to your os environment variable

Neo4j:

- export `NEO_USER` and `NEO_PSW` to your os environment variable
- if you put neo4j database locally working with CRDD, skip steps next in this part
- if your neo4j is remote, set your neo4j configurations to ./CRDD/settings.py `NEO4J`

frontend:

- add your vue address to ./CRDD/settings.py `CORS_ALLOWED_ORIGINS`, default `localhost:5173`

run:

- `python manage.py migrate` to initialize your MySQL, `python manage.py runserver` to run the backend

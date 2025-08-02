# CRUD con Django y PostgreSQL

Este proyecto es una aplicación web tipo CRUD (Create, Read, Update) para administrar registros de nombre y correo electrónico, desarrollado con **Django** y conectado a una base de datos **PostgreSQL**.

---

## Tecnologías utilizadas

- Python 3.10+
- Django 5.2.4
- PostgreSQL
- Django ORM (protegido contra inyecciones SQL)
- python-dotenv (para gestión segura de credenciales)

---

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener lo siguiente instalado:

| Herramienta           | ¿Obligatorio? | Instalación recomendada                       |
|-----------------------|---------------|-----------------------------------------------|
| Python 3.13.5         | Sí            | https://www.python.org/downloads/             |
| PostgreSQL 17.5.3     | Sí            | https://www.postgresql.org/download/          |
| Git 2.50.1            | Sí            | https://git-scm.com/downloads                 |

---

## Instalación paso a paso

### 1. Clona el repositorio

git clone https://github.com/malvamo/crud-django-postgresql-admin.git

cd crud-django-postgresql

### 2. Crea y activa un entorno virtual

python -m venv env

En Linux: source env/bin/activate      

En Windows: env\Scripts\activate

### 3. Instala las dependencias

pip install -r requirements.txt

### 4. Configuración de PostgreSQL (Crear base de datos y usuario)

Antes de ejecutar las migraciones, asegúrate de que la base de datos y el usuario existen en PostgreSQL y tienen permisos adecuados.

## Opción 1: Desde la terminal (psql)

### Abre la terminal y entra al cliente:

psql -U postgres

Te pedirá la contraseña de tu usuario PostgreSQL (por defecto es postgres).

### Crea la base de datos:

CREATE DATABASE crud_data;

### Crea el usuario:

CREATE USER admin WITH PASSWORD 'admin';

### Concede privilegios al usuario:

GRANT ALL PRIVILEGES ON DATABASE crud_data TO admin;

Cambiar a esa base de datos

\c crud_data

Otorgar acceso al esquema público (donde Django crea sus tablas)

GRANT ALL ON SCHEMA public TO admin;

### Sal del cliente:

\q

### Opción 2: Usando pgAdmin (Interfaz gráfica)

Abrir pgAdmin e iniciar sesión.

Crear la base de datos crud_data:

Navega a Databases > clic derecho > Create > Database...

En el campo Database, escribe: crud_data

Owner: postgres

Clic en Save

Crear el usuario admin:

Ve a Login/Group Roles > clic derecho > Create > Login/Group Role...

En la pestaña General: nombre admin

En Definition: contraseña admin

En Privileges: activa LOGIN, CREATE, CONNECT

Guardar

Asignar permisos sobre la base de datos:

En Databases > crud_data, clic derecho > Properties > Privileges

Agrega el rol admin

Marca todos los privilegios: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER

Guardar

Dar permisos sobre el esquema public:

En crud_data > Schemas > public, clic derecho > Properties > Privileges

Agrega el rol admin

Marca al menos: USAGE, CREATE

Guardar

### 5. Aplica las migraciones para crear las tablas

python manage.py migrate

### 6. (Opcional) Crea un superusuario

python manage.py createsuperuser

### 7. Ejecuta el servidor

python manage.py runserver

Abre en tu navegador:

http://127.0.0.1:8000/ → Página principal del CRUD

http://127.0.0.1:8000/admin/ → Panel administrativo


### Seguridad

Las credenciales de la base de datos se guardan en un archivo .env y no se suben al repositorio.
El proyecto utiliza el ORM de Django, que protege automáticamente contra inyecciones SQL (SQLi).
El formulario valida los campos antes de guardar y escapa contenido en las plantillas.

### Consideraciones

El proyecto no incluye datos precargados, pero puede funcionar desde cero con solo ejecutar migraciones.
Todo el código está desacoplado por responsabilidad (Modelo, Vista y Plantilla), siguiendo el patrón MTV/MVC.
Puedes modificar los estilos fácilmente agregando tus propios archivos CSS en la carpeta static/.

### Autor

Desarrollado como prueba técnica.
Sustentado por: Manuel Valbuena
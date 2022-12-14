# calyx-challenge
 
##### Pre-requisitos:
- Sistema operativo: Linux (Ubuntu 18.04 LTS)
- [Python 3.6](https://www.python.org/downloads/release/python-360/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

(Opcional) si se quiere consultar la Base de Datos, se recomiendan:
- [DataGrip](https://www.jetbrains.com/datagrip/)
- [DockerCompose](https://docs.docker.com/compose/install/)

##### Setup:
- Clonar el repositorio
- Posicionarse en la carpeta raíz del proyecto
- Crear un virtualenv: python3 -m venv /path/to/new/virtual/environment.
- Ingresar al entorno virtual: source /path/to/new/virtual/environment/bin/activate
- Instalar las dependencias: pip install -r requirements.txt
- Crear un archivo .env en la raíz del proyecto con las siguientes claves:
    - POSTGRES_USER (usuario de postgres)
    - POSTGRES_PASSWORD (contraseña de postgres)
    - POSTGRES_DB (nombre de la base de datos)
    - POSTGRES_HOST (host de postgres)
    - ENABLE_DATABASE_CREATION (True o False, si se quiere crear la base de datos) (si se corre a nivel local, dejar en True)

OBSERVACIÓN!: asegurarse de que el usuario de postgres tenga permisos para crear bases de datos, y de que la contraseña sea la correcta.

##### Ejecución:

- Ingresar al entorno virtual (si es necesario): source /path/to/new/virtual/environment/bin/activate
- Exportar las variables de entorno: export $(cat .env | xargs)
- En el directorio raíz, ejecutar el comando: python app.py
- Los archivos se guardan en la carpeta stored_data, y luego de acuerdo al formato del enunciado
- Los logs de ejecución se encuentran en el archivo logs/app.log
- Si se quiere consultar la Base de Datos (a nivel local):
    - Ejecutar el comando: docker-compose up db
    - Cofigurar la conexión a la Base de Datos desde DataGrip, de acuerdo a los datos del archivo .env
    - Ingresar a la Base de Datos y verificar que se hayan creado las tablas y se hayan cargado los datos.





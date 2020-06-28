# Diccionario

Webapp para crear un diccionario online, en el cual se puede agregar, editar y eliminar terminos y sus deficioniciones, disenado con Django como framework y postgresql como motor de base de datos.

# Tabla de Contenido
1. [Dependencias.](#)
2. [Instalacion del proyecto.](#Intalacion)
3. [Iniciar el servidor web.](#Iniciar-el-servidor-web)

## Dependencias
1. [Django.](#https://www.djangoproject.com/)
2. [PostgreSQL](#https://www.postgresql.org/)

## Instalacion
1. Clonar el proyecto.
2. Usa el administrador de paquete [pip](https://pip.pypa.io/en/stable/) para instalar los requerimientos de la webapp.

```bash
pip install -r requirements.txt
```
3. Configura las credenciales de postgresql en la seccion DATABASES del archivo project/project/setting.py
4. Crear las migraciones de la base de datos.
```bash
cd project
python manage.py makemigrations
python manage.py migrate
```
5. Importa el backup de las letras del diccionario a la base de datos.

## Iniciar el servidor web
1. Entra al directorio del proyecto.
```
cd project
```
2. Iniciar el servidor web
```bash
python manage.py runserver
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

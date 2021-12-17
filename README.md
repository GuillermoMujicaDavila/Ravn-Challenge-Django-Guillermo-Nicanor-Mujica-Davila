# Ravn-Challenge-Django-Guillermo-Nicanor-Mujica-Davila
● Descripcion:
El siguiente codigo fue creado para poder resolver el reto de Ravn, el cual consiste en un desarrollo de Back-End como Front-End, el programa tienen la capacidad de listar las personas de un determinado genero.

●   Setup/Running instructions
- Descargue las fuentes
- Genere el entorno virtual para poder utilizarlo con el siguiente comando: py -m venv <<Nombre_del_entorno_virtual>>
- Ejecute su entorno virtual ingresando a su ambiente utilice los siguientes comandos:
        * cd <<Nombre_del_entorno_virtual>>/Scripts
        * .\activate
- Instale los paquetes necesarios: 
        * pip install -r requirements.txt
-Cree un archivo .env dentro de la carpeta Project y agregue las siguientes variables
    DB_HOST=
    DB_USERNAME=
    DB_PASSWORD=
    DB_PORT=
    DB_NAME=
    DB_TEST=
-Genere la migración en la consola con py manage migrate (La ruta tiene que estar dentro de Project). ej:
    Ravn-Challenge-Django-Guillermo-Nicanor-Mujica-Davila\project
-Genere su superUsuario con:
    py manager.py createsuperuser
-Ejecute el aplicativo con
    py manage.py runserver

●	Hay una carpeta con la fotos de como funciona el aplicativo, junto un json que puede ejecutar en postaman 
●	Technologies used
- Python (Django)
- VisualStudio Code
- Postgresql


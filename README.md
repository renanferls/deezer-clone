 # Deezer Clone 

<hr>


[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

## Header <a name = "header"></a>
Sistema desarrollado para simular el comportamiento del sistema de streaming de musica [Deezer](https://www.deezer.com/es/), con funcionalidad de autenticacion para usuarios como registro, login y logout.

# Contenido

- [Acerca del proyecto](#acerca)
- [Autor](#autor)
- [Deployment](#deployment)
- [Modo de uso](#uso)
- [Justificacion de endpoint propuestos](#justificacion)

## Acerca del proyecto <a name = "acerca"></a>

### **Herramientas utilizadas para el desarrollo del sistema**
* _[Python v3.10](https://www.python.org/)_
* _[Django v4.1](https://www.djangoproject.com)_
* _[Django Rest Framework v3.14](https://www.django-rest-framework.org/)_

### **Descripcion**
Proyecto que forma parte del reto tecnico de [Silabuz](https://www.silabuz.com/) para el puesto de Backend Imparable.

[Ver descripcion](#header)

## Autor <a name = "autor"></a>

- [@renanferls](https://github.com/renanferls)

## Prerequisitos <a name = "prerequisitos"></a>

Para la ejecucion del proyecto se necesitan las herramientas descritas anteriormente

## Despliegue
A continuacion se explica el proceso para realizar el despliegue del proyecto

Como primer paso crear un entorno virtual para aislar el proyecto y ejecutarlo, una vez listo proceder a instalar las dependencias desde el archivo requirements.txt con el siguiente comando:

```
pip install -r requirements.txt
```

Una vez listo, ejecutamos:

```
python manage.py makemigrations
python manage.py migrate
```

Esto para realizar las migraciones correspondientes en caso no se hayan actualizado.


Para ejecutare el servidor usar el comando:

```
python manage.py runserver
```
Esto hara que se ejecute el servidor en el puerto 8000, por defecto para Django

<hr>


## Modo de uso <a name="uso"></a>
Una vez que este en ejecucion, abrir el navegador con la direccion [127.0.0.1:8000](127.0.0.1:8000) el cual mostrara los endpoints creados para el proposito del proyecto e interactuar con ellos.

<hr>

## Justificacion de endpoints propuestos <a name="justificacion"></a>

- Los siguientes edpoints se generaron de manera que su uso esta orientado basicamente a un CRUD para cada modelo/tabla de la base de datos. Asi como tambien la funcionalidad de la autenticacion.

<hr>

1. [api/schema/](#explain1&2)
2. [api/schema/swagger-ui/](#explain1&2)
3. [api/schema/redoc/](#explain1&2)
4. [admin/](#admin)
5. [api/](#api)
6. [api/auth/](#auth)

<hr>

## Los cuales se proceden a explicar en lo siguiente:

<hr>


## Desc. 1. | 2. | 3. <a name="explain1&2&3"></a>

1. Este endpoint permite realizar la descarga de un archivo en formato [yaml](https://yaml.org), en el cual se detalla todo lo que se ha documentado.

2. Este endopoint, permite la visualizacion e interaccion con la interfaz de [Swagger/OpenAPI](https://swagger.io/) para apreciar los diferentes endpoints creados.

3. Similar al punto anterior permite interactuar con los procesos pero con una interfaz mas ordenada y detallada.

<hr>

## Desc. 4. - Admin Site <a name="admin"></a>
4. Este endpoint permite la interaccion con el dashboard generado automaticamente por Django, en el cual se puede ver los modelos y/o tablas creadas, permisos, niveles de acceso, etc.

<hr>

## Desc. 5. - Deezer API <a name="api"></a>
5. Este viene a ser el path para acceder a los procesos CRUD de las tablas consideradas para realizar los solicitado en el reto. Los modelos considerados son:
    - artist
    - album
    - genre
    - track

Adicional a ello se tienen dos procesos de busqueda de album y artista, y tambien un buscador "general"

## Desc. 6. - Auth API <a name="auth"></a>
6. Path para acceder a los endpoints correspondientes a la interaccion con el usuario, se tienen los siguientes:
    - registration or signup
    - login
    - logout
    - profile


<hr>

## **--- ATENCION ---**
## Para ingresar a la documentacion de Swagger con interfaz grafica abrir cualquiera de los siguientes endpoints:
- http://127.0.0.1:8000/api/schema/swagger-ui/
- http://127.0.0.1:8000/api/schema/redoc/

Asi mismo se adjunto un archivo para ser importado desde [POSTMAN](https://www.postman.com/) para probar cada uno de los endpoints desde alli.

<hr>

## **DISCLAIMER**
Se ha usado [drf-spectacular](https://drf-spectacular.readthedocs.io) como integracion de OpenAPI para el proyecto actual, el cual permite realizar la autenticacion en la capa de interfaz generada, se han testeado todos los modulos de manera satisfactoria; sin embargo, el logout "no funciona" debido a que el tema del token se maneja a nivel de base de datos (sesion), lo cual al parecer la herramienta no soporta dicha funcion.

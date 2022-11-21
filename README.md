# BBBBB5
Proyecto Colaborativo - ISPC 2022 - Grupo BBBBB5

![Image text](https://github.com/ispc-programador2022/BBBBB5/blob/main/banner.jpg)

##################################################################################

Los archivos "POOBBDD.py" y "conexion.php" ubicados dentro de la carpeta "modulos" poseen como acceso a la base de datos la siguiente información:

  SERVIDOR:       "localhost"
  USUARIO:        "root"
  CLAVE:          "" <- sin clave
  BASE DE DATOS:  "Proy_Colab_BBBBB5"

Los datos de usuario son los que vienen por defecto en la instalación de MySQL en los diferentes programas que funcionan como servidores web locales como XAMPP, WAMPP, LAMPP, Laragon (Laragon.org) o similares.

##################################################################################

El archivo "__init__.py" ubicado también en la carpeta "modulos" no contiene ningún contenido y sólo se encuentra allí para que python reconozca que los módulos de extensión ".py" allí ubicados pueden ser invocados desde el sistema de una carpeta superior mediante la sentencia "import"

##################################################################################

Se incluye un archivo "Estructura de la BBDD proy_colab_bbbbb5.sql" en el directorio raíz con información para la creación de la BBDD que alojará la información reunida por el sistema de web scraping.
A la vez, se incluyó en el archivo "libros.sql" un listado con más de 800 registros reunidos en una prueba realizada (de los casi 40.000 libros existentes en la tienda elegida) para poder trabajarlos. Excedernos en la cantidad de libros produciría una falla a nivel del servidor Apache y de las variables de PHP que no tenían que ver con el proyecto, por eso limitamos la cantidad de registros de la muestra a una cantidad relativamente manejable pero considerable para los fines del ejercicio.

##################################################################################

Equipo BBBBB5 conformado por (en orden alfabético):

Baravaglio, Raimundo | Belen, Esteban | Bellesi, Filomena | Benitez, Daniel | Bolatti Cristofaro, María Carolina

##################################################################################

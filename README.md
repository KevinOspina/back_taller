
## Instrucciones para Django

### Crear ambiente virtual
1. Instalar virtualenv con el comando __pip install virtualenv__
2. Crear el ambiente virtual con el comando __virtualenv ENV__

### Activar ambiente virtual
Windows: ENV\Scripts\activate

Linux: source ENV/bin/activate

Si funcionó al lado de la terminal se mostrará (ENV)
Para salir del ambiente virtual solo hay que escribir deactivate.

En PyCharm esto no es necesario.


## Instalar dependencias
Usar el siguiente comando **pip install -r requirements.txt**

Con lo anterior ya se tiene listo el ambiente de trabajo para trabajar.

## Correr aplicación
Correr el siguiente comando, luego de haber ingresado al ambiente virtual
**python manage.py runserver**

En PyCharm se puede correr desde el botón de ejecución.

# Instrucciones para Git

## Actualizar repositorio
git pull

## Mandar cambios
1. git add .
2. git commit -m "< Mensaje sobre el commit >"
3. git push

## Combinar cambios con master
Esto se hace desde github en la opción pull requeste, se le debe mandar notificación de revisión a todos los miembros.

# Instrucciones base de datos

El usuario está configurado como marteoma, pueden crear un usuario con este nombre,
o configurar las settings, pero no suban el archivo con estas. 

1. Abrir la terminal de psql, esto ya sea con la que viene al instalar, o desde la terminal si está en el PATH
2. Usar el comando **CREATE DATABASE meejel;** No olvidar el _';'_
3. Usar el comando **\c framework** Esto selecciona la base de datos

Con esto ya tienen la base de datos creada y seleccionada para trabajar en la terminal.
La terminal servirá principalmente como fuente de información, todo se hará desde Django.

## Comandos útiles de la terminal PSQL

* **_\\! cls_** Limpia la terminal en Windows
* **_Ctrl + L_** Limpia la terminal en Linux
* **_\d_** Listar tablas de la base de datos
* **_\c database_** Selecciona la base de datos especificada
* **_\l_** Listar todas las bases de datos

Adicionalmente se puede usar cualquier sentencia SQL directamente.
Adicional a esto, si ya tienen el usuario de postgres configurado, deben configurar el usuario
para que el USER sea _postgres_, el PASSWORD sea también _postgres_ y esté en el puerto _5432_
ya que así se aplicó la configuración a Django.

## Migraciones

Para realizar las migraciones, se hace lo siguiente
1. Primero que todo se debe estar situado dentro de MEEJEL en la terminal, al mismo nivel de manage.py
2. Usar el comando **py manage.py makemigrations**
3. Usar el comando **py manage.py migrate**
4. Si todo sale bien, en el terminal de psql, usando la base de datos framework, al buscar las 
tablas (\\d) aparecerá una lista de tablas generadas por Django, en caso contrario, revisar que todo
en la base de datos se cumpla.

## Aviso

Este sistema fue hecho con propósitos educionales y gratis, si lo ve en un lugar comercial, por favor informenos.

Este sistema fue hecho por:
* Mateo Arboleda Roldán: marteoma@github.com
* Cristhian Chica Acosta: cca00@github.com
* Sebastián Mejía: mcMEJIA1@github.com


###### FUTURO

Esta en desarrollo una versión dockerisada para más fácil ejecución.

# Acerca de este proyecto

El objetivo principal de este proyecto es tener una plataforma donde puedas calificar álbumes de música para
los artistas que estarán disponibles. En esta plataforma encontrarás las carátulas de los álbumes
y habrá un cuadro de comentarios donde puede dejar sus comentarios al respecto y también calificar
los álbumes del 1 al 10.
# Modelado de datos

## Entidades

- Artista(id_artist)
El artista sera la entidad que contenga los nombres de los artistas disponibles para poder desplegar la lista de los albums.

- Albums(album_id)
Los albums son la entidad que contiene la lista de los albums disponibles por artista.

- Usuario(user_id)
Este sera necesario para identificarse dentro de la plataforma.

# Consulta de datos

- Consulta de información
		- Por Artistas
		- Por Albums

- Consulta en general
		- Lista completa de Artistas
		- Lista completa de Albums


# Como funciona

| Path								| Description     |
|-----------------------------------|-----------------|
|/musiclife/login					| Esta es la ruta donde encontrará el inicio de sesión.
|/musiclife/artists_list				| En este camino encontrarás la lista de artistas disponibles.
|/musiclife/albums_lists_artist 		| Esta es la ruta de los álbumes disponibles de un solo artista.
|/musiclife/user/add					| Esta es la ruta para agregar un nuevo usuario.
|/musiclife/albums					| Esta es la ruta que desplegara una lista con todos los albums disponibles.

# Archivos relacionados

- `routes/musiclife.py`

- `modules/musiclife.py`


# Estructura de API

- Artist(id_artist)
- Album(album_id)
- User(user_id)
- Comment and rate(album_id, user_id, rate, date)


# Operaciones de almacenamiento de datos

### Operación del usuario

- Nombre y contraseña.

- El ID se generará automáticamente.

### Operación del álbum

- El álbum que está seleccionado, mostrará un cuadro de comentarios y un cuadro de rango donde el usuario podrá calificar de 1 a 10.


# Consulta de datos

  - Lista de artistas
	- Lista de albums
	- Comentarios en albums


# Estructura de solicitud y respuesta

### Registro de usuario
```
{
	"name": "David Cruz Zepeda"
	"password" "1234567"
}
```
### Respuesta de ID de registro exitosa
```
{
	"id": "00001"
}
```
### Registro de comentarios y valoraciones
```
{
	"comment": "This album in my opinion has a nice rap bars, and the melody is very dope, I hope Freddie Dredd dont loose the flow and style"
	"rate": "10"
	"date": "2021-04-23T18:25:43.511Z"
	"user_id": "0001"
}
```
### Respuesta exitosa del registro de comentarios
```
{
	"id": Comment + "0001"
}
```

### Implementación de rutas de recursos


`POST /musiclife/artist/albums_lists_artist/comment` : Esto registrará el comentario, la calificacion y la fecha.

`GET /musiclife/artists_list` : Esto solicitará la lista de los artistas disponibles.

`GET /musiclife/albums_lists_artist` : Esto solicitará la lista de los álbumes disponibles del artista.

`GET /musiclife/albums` : Esto solicitara la lista de todos los albums disponibles.

`POST /musiclife/user/add` : Esto registrará un nuevo usuario.

#Documento de plan de implementación

# Pasos de implementación en general (Aspecto general)

### Descripción general del problema

Este proyecto ayudará al público en general, al tener una calificación y comentarios sobre
los álbumes del artista. La mayor parte de las veces la gente no sabe lo que la gente
piensa en un álbum o la calificación.

### Motivación del proyecto

Este proyecto fue motivado por la necesidad de tener una fuente donde poder encontrar la calificación,
y comentarios sobre los álbumes de música, con la esperanza de tener algún comentario sobre el conjunto
música, dando una referencia, de lo que el público en general puede esperar encontrar en el
artista de un album. Para las personas que hacen música este proyecto será útil porque pueden
encontrar las mejores muestras, o conocer las voces, características, etc.

### ¿Quién es el público afectado por el problema que solucionó este proyecto?

Este proyecto ayudará a los productores de música y al público en general a traerles una página web,
donde pueden encontrar información sobre los álbumes de música de los artistas disponibles.

### Solución específica de este proyecto

La solución proporcionará información sobre los álbumes de música que desarrollan los artistas,
esta información funcionará como referencia de lo que el público puede encontrar en el álbum.
Esto ayudará a los productores musicales a tener cierta información sobre qué tipo de muestras
alguien puede encontrar, la voz, la instrumental, etc., etc.

### Recursos humanos, recursos informáticos e infraestructura.

Para este proyecto necesitaremos una recopilación masiva de las portadas de los álbumes que cada
artista tiene sobre la existencia, por lo que de esa manera el proyecto tuvo una amplia variedad de géneros de música,
igual que artista, álbumes, etc.

Para los recursos informáticos, necesitaremos un servidor dedicado donde ejecutamos un servidor HTTP. Y
otros servicios que serán necesarios para brindar el servicio. También necesitaremos una base de datos donde
debe almacenar todos los comentarios, calificaciones, usuarios y fechas.

# Aspecto Tecnico

### Modulos de codigo necesarios

- Rutas: Las rutas son necesarias para que brinden una estructura a la pagina al momento de navegar por la pagina.

- Almacenamiento: Es necesario que existan funciones para poder almacenar el texto que sera introducido en los cuadros de texto.

### Metodos de almacenamiento

- Para el almacenamiento se requiere de un sistema de archivos local.

## Plan para la codificacion de los Modulos

El modulo para almacenamiento debe de ser creado de manera que se puedan almacenar los datos satisfactoriamente. Es necesario realizar una funcion que no deje puertas traseras a errores.

## Plan para la verificacion del producto

Una vez concluido el proyecto se tendran que realizar pruebas para serciorarse de que el funcionamiento es correcto. De igual manera se haran pruebas para encontrar posibles errores que el usuario final podria provocar.


# Computo en la nube

1. Crear Fork del proyecto storage-API

Aqui se señala cual es el commit a partir de donde se realizo el fork.

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de Fork|   b7ad51029eb46ed9c48170f52c80c906173f3e72

2. Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de docs/musiclife.md|   ef097c4125eec5b0e0d73212ac05e986b5df5904

3. Creacion de documento con las rutas.

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de routes/musiclife.py|   7a17635b39a28d9fa42a5c13160c05daac4e4a41

4. Creacion de documento de funciones

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de modules/musiclife.py|   4ccfa193574286b51a76475318f94497be1ddebe


5. Creacion de Mock Ups

| Concepto                 | Commit Hash|
| --------------------- | ----------- |
|  Creacion de /docs/assets/|   948608729216ffaf2316004ef2b6f5cd0a5d5639

## Explicacion de Mock Ups
![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Inicio%20Music%20Life.png)
Dentro de la ruta /docs/assets en la imagen `Mock Up Inicio Music Life.png` podremos encontrar la estructura deseada de la pagina, que sera el inicio. Donde tendremos los botones de Artistas, Albums, una barra de busqueda, asi como una seccion donde se encontrara el contenido mas nuevo.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Lista%20de%20Artistas.png)
Dentro de la imagen `Mock Up Lista de Artistas.png` se desplegara la lista de los artistas que se encuentren disponibles al momento de dar click en el boton de artistas.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Lista%20de%20Albums%20de%20Artista.png)
Posteriormente en la imagen `Mock Up Lista de Albums de Artista.png` al dar click sobre el nombre de algun artista este redirigira a una pagina donde se mostraran la lista de los albums disponibles del artista.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Agregar%20Comentario%20Album.png)
Por ultimo en el Mock Up `Mock Up Agregar Comentario Album.png` se observara la manera en que se mirara al momento de querer ingresar un nuevo comentario y calificación al album del artista elegido, de igual manera una vez entrando al album se desplegaran los comentarios ya existentes acerca del album.


*-*-*-*-*-*-*-*-*-*

# Casos de uso

- # 1 El usuario desea agregar un Artista Nuevo.

 - Para completar la accion el usuario debera ingresar los campos requeridos para almacenarlo los cuales son: id_artist y genre.
 - En dado caso que el usuario registre datos invalidos, se le mostrara un error 400 con el mensaje
   "Datos invalidos"

 - Ejemplo de curl de registro exitoso con POST:
```
curl http://localhost:8081/musiclife/artists -X POST -H 'Content-Type: application/json' -d '{"id_artist": "Ice Cube", "genre": "RAP"}'
```

- # 2 El usuario desea agregar un Album Nuevo.

- El usuario debera de ingresar los campos requeridos para almacenarlo, los cuales seran id_artist, album_id y genre.
 - En dado caso de que el usuario registre datos invalidos, se le mostrara un error 400 con el mensaje
   "Datos Invalidos"

 - Ejemplo de curl de registro exitoso con POST:
```
curl http://localhost:8081/musiclife/albums -X POST -H 'Content-Type: application/json' -d '{"id_artist": "Freddie Dredd", "album_id": "Dredd", "genre2": "RAP"}'
```

 - # 3 El usuario desea agregar un nuevo comentario a cierto album.

  - El usuario debera ingresar los campos requeridos para almacenarlo, los cuales son comment y range.
  - Los demas campos del curl se agregaran automatico ua vez dado el click en el boton de guardar comentario, tales campos seran
    id_artist, review_id, user_id, album_id.
 - En dado caso de que el usuario registre datos invalidos, se le mostrara un error 400 con el mensaje
   "Datos Invalidos"

 - Ejemplo de curl de registro exitoso con POST:

```
curl http://localhost:8081/musiclife/review -X POST -H 'Content-Type: application/json' -d '{"review_id": "008", "user_id": "009", "album_id": "Freskibon", "id_artist": "Metrik Vader", "rate": "5", "comment": "pura rola chida desde cancun"}'
```

 - # 4 El usuario desea consultar todos los artistas disponibles.

  - En estos casos el id_artist sera el identificador con el que se podra consultar la informacion.
  - En dado caso de que el usuario utilize un identificador no existente se marcara un error 500 con el mensaje
	"Error Interno"

  - Ejemplo de curl para una consulta especifica con GET

```
curl http://localhost:8081/artists -X GET
```

 - # 5 El usuario desea consultar todos los albums disponibles.

  - En estos casos el album_id sera el identificador con el que se podra consultar la informacion.
  - En dado caso de que el usuario utilize un identificador no existente se marcara un error 500 con el mensaje
	"Error Interno"

  - Ejemplo de curl para una consulta especifica con GET

```
curl http://localhost:8081/albums -X GET
```

 - # 6 El usuario desea consultar todos los comentarios de un album disponible.

  - En estos casos el album_id sera el identificador con el que se podra consultar la informacion.
  - En dado caso de que el usuario utilize un identificador no existente se marcara un error 500 con el mensaje
	"Error Interno"

  - Ejemplo de curl para una consulta especifica con GET

```
curl http://localhost:8081/albums/8_Ball_Playas/review -X GET
```

# Planeacion para desarrollo de Front-end

Para el desarrollo de este se requerira un maquetador para que el diseño de la pagina sea de lo mas apropiado para el
tipo de proyecto que representa y deje a futuro espacio para nuevas funciones.
Mediante el uso de HTML, CSS y JavaScrip se crearan los debidos archivos donde dentro de estos se contendra funciones, asi como
el diseño, se configurara que la pagina sea dinamica de tal manera que funcione en Navegadores Web de PC y de telefonos.

- Para el debido funcionamiento el servidor debera procesar las consultas para GET, UPDATE y POST, de las siguientes identidades
dentro de el Storage-API, Artista y Album.
- Se requiere que las validaciones para el almacenamiento de datos incorrectos este definido para evitar complicaciones en
las consultas de informacion que se requiera.

- Se requiere que el inicio de sesion de la pagina funcione correctamente y que le asigne a los usuarios los permisos correspondientes
conforme a su nivel de jerarquia.

## Para el diseno del login se propone lo siguiente:

Se presentaran dos campos, donde vendra con texto adentro de user name y password, las cuales seran las credenciales del usuario,
posteriormente estas se autentificaran con el boton de ingresar a sesion.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Login.png)

## Para la pagina inicio se propone lo siguiente:

Que se reciba con un cuadro de texto donde se encuentre los artistas mas recientes, asi como dos botones uno de lista de artistas y lista de albums.


![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Inicio%20Music%20Life.png)

## Una vez dado un click en Artistas, se redirigira a una pagina donde se tendra la lista de los artistas disponibles.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Lista%20de%20Artistas.png)

## Para la siguiente pagina se seleccionara un artista y la pagina de albums desplegara una lista de los albums disponibles.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Lista%20de%20Albums%20de%20Artista.png)

## Una vez seleccionado el album se observara el album y se encontrara el cuadro de texto donde se insertara el comentario asi como
un medidor donde seleccionara la calificacion del album.

![Login](https://github.com/DavidCroix/storage-api/blob/0114cb96fe665363fb786cb5e3abd08e282ecd9b/docs/assets/Mock%20Up%20Agregar%20Comentario%20Album.png)

# Documentacion para continuar el trabajo

Para el posible continuo desarrollo del proyecto se tienen en consideracion la correccion y creacion de los siguientes pendientes:

Las rutas donde se almacenan los JSON de artista y de albums tienen que ser corregidos en el archivo que se encuentra en la ruta, ``` /modules/musiclife.py ``` de igual manera cada uno de los id de la variable ``` almacenable ``` se tienen que verificar que esten con el mismo nombre, que en el archivo en la ruta ``` /routes/musiclife.py ```. Se deberan realizar pruebas con los CURL y con los print verificar que la variable de nombre ``` almacenable ``` este recibiendo los argumentos debidamente, para verificar que la funcion si sirve.

Se deberan replantear la manera en la que operan los CURL de GET, ya que las rutas aun no han sido completamente definidas,
y esto da lugar a que el lugar donde se manda el JSON almacenable no sea la ruta debida y por lo tanto se tenga un conflicto al accionar la funcion, y esta no tenga la ruta determinada para hacer la consulta.

Se deberan realizar diversas funciones para que los campos donde el usuario interactue se encuentren fuera de
fallos, ya sea por contenido agregado, o por algun otro error que pueda pasar desapersivido. Otra de las demas
funciones que deberan desarrollarse seran las funciones para el incremento automaticamente tanto del id de usuario,
tanto como del numero de comentario, para tener un mejor control y una manera mas sencilla de acceder a los datos en
dado caso que se requiera hacer una consulta.


De igual manera se debera realizar algun tipo de funcion para que los usuarios tengan ciertos permisos y 
privilegios conforme al rango del usuario, esto para evitar que realizen actos no debidos.

Se debera desarroollar CURL de busqueda por id, ya se de algun artista o album que se encuentre en existencia, asi
como por numero de comentario y por id de albums.

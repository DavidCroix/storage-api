# Acerca de este proyecto

El objetivo principal de este proyecto es tener una plataforma donde puedas calificar álbumes de música para
los artistas que estarán disponibles. En esta plataforma encontrarás las carátulas de los álbumes
y habrá un cuadro de comentarios donde puede dejar sus comentarios al respecto y también calificar
los álbumes del 1 al 10.

# How it works.

| Path								| Description     |
|-----------------------------------|-----------------|
|/musiclife/login					| Esta es la ruta donde encontrará el inicio de sesión.
|/musiclife/artists_list				| En este camino encontrarás la lista de artistas disponibles.
|/musiclife/albums_lists_artist 		| Esta es la ruta de los álbumes disponibles de un solo artista.
|/musiclife/user/add					| Esta es la ruta para agregar un nuevo usuario.


# Archivos relacionados

- `routes/musiclife.py`

- `modules/musiclife.py`


# Estructura de API

- Artist(id_artist)
- Album(album_id, id_artist, genre, release_date)
- User(user_id)
- Comment and rate(album_id, user_id, rate, date)


# Operaciones de almacenamiento de datos

### Operación del usuario

- Nombre y contraseña.

- La identificación se generará automáticamente.

### Operación del álbum

- El álbum que está seleccionado, mostrará un cuadro de comentarios y un cuadro de rango donde el usuario podrá calificar de 1 a 10.


# Consulta de datos

- Solicitud de artista
	- Albums
	-Comment
	-Genre

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
}
```
### Respuesta exitosa del registro de comentarios
```
{
	"id": Comment + "0001"
}
```

### Implementación de rutas de recursos


`POST /musiclife/artist/albums_lists_artist/comment` : Esto registrará el comentario, la tasa y la fecha.

`GET /musiclife/artists_list` : Esto solicitará la lista de los artistas disponibles.

`GET /musiclife/albums_lists_artist` : Esto solicitará la lista de los álbumes disponibles del artista.

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
debe almacenar todos los comentarios, tarifas, usuarios y fechas.

# Aspecto Tecnico

### Modulos de codigo necesarios

- Rutas: Las rutas son necesarias para que brinden una estructura a la pagina al momento de navegar por la pagina.

- Almacenamiento: Es necesario que existan funciones para poder almacenar el texto que sera introducido en los cuadros de texto.

### Metodos de almacenamiento

- Para el almacenamiento solo se requiere una funcion para guardar el texto en forma `string` .

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
![Login](https://github.com/DavidCroix/storage-api/blob/948608729216ffaf2316004ef2b6f5cd0a5d5639/docs/assets/Mock%20Up%20Inicio%20Music%20Life.png)
Dentro de la ruta /docs/assets en la imagen `Mock Up Inicio Music Life.png` podremos encontrar la estructura deseada de la pagina, que sera el inicio. Donde tendremos los botones de Artistas, Albums, una barra de busqueda, asi como una seccion donde se encontrara el contenido mas nuevo.

![Login](https://github.com/DavidCroix/storage-api/blob/1e02710332aca970fd168249329c7bb96c7b2777/docs/assets/Mock%20Up%20Lista%20de%20Artistas.png)
Dentro de la imagen `Mock Up Lista de Artistas.png` se desplegara la lista de los artistas que se encuentren disponibles al momento de dar click en el boton de artistas.

![Login](https://github.com/DavidCroix/storage-api/blob/1e02710332aca970fd168249329c7bb96c7b2777/docs/assets/Mock%20Up%20Lista%20de%20Albums%20de%20Artista.png)
Posteriormente en la imagen `Mock Up Lista de Albums de Artista.png` al dar click sobre el nombre de algun artista este redirigira a una pagina donde se mostraran la lista de los albums disponibles del artista.

![Login](https://github.com/DavidCroix/storage-api/blob/1e02710332aca970fd168249329c7bb96c7b2777/docs/assets/Mock%20Up%20Agregar%20Comentario%20Album.png)
Por ultimo en el Mock Up `Mock Up Agregar Comentario Album.png` se observara la manera en que se mirara al momento de querer ingresar un nuevo comentario y calificación al album del artista elegido, de igual manera una vez entrando al album se desplegaran los comentarios ya existentes acerca del album.

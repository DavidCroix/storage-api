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

# Pasos de implementación en general (descripción general)

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

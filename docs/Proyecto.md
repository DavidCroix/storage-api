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

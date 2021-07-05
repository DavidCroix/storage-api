# About this project


The main goal of this project is to have a platform where you can rate music albums for
the artists that will be available. In this platform you will find the albums covers
and there will be a comment box where you can leave your comments about it, and also rate
the albums from 1 to 10.

# How it works.

| Path								| Description     |
|-----------------------------------|-----------------|
|/musiclife/login					| This is the path where you will find the Login.
|/musiclife/artists_list				| In this path you will find the list of the artist available.
|/musiclife/albums_lists_artist 		| This is the path of the albums available of a single artist.
|/musiclife/user/add					| This is the path to add a new user.


# Related Files

- `routes/musiclife.py`

- `modules/musiclife.py`


# Structure of API

- Artist(id_artist)
- Album(album_id, id_artist, genre, release_date)
- User(user_id)
- Comment and rate(album_id, user_id, rate, date)


# Storage Data Operations

### User Operation

- Name and password.

- The ID will be generated automatictilly.

### Album Operation

- The album that is selected, it will display a comment box and a range box where the user will be able to rate from 1 to 10.


# Query Data

- Request Artist
	- Albums
	-Comment
	-Genre

# Request and Respond Structure

### User Register
```
{
	"name": "David Cruz Zepeda"
	"password" "1234567"
}
```
### Succesful Register ID Response
```
{
	"id": "00001"
}
```
### Comment and Rate Register
```
{
	"comment": "This album in my opinion has a nice rap bars, and the melody is very dope, I hope Freddie Dredd dont loose the flow and style"
	"rate": "10"
	"date": "2021-04-23T18:25:43.511Z"
}
```
### Succesful Comment Register Response
```
{
	"id": Comment + "0001"
}
```

Resources Routes Implementation


`POST /musiclife/artist/albums_lists_artist/comment` : This will register the comment, rate and date.

`GET /musiclife/artists_list` : this will request the list of the available artists.

`GET /musiclife/albums_lists_artist` : This will request the list of the available albums of the artist.

`POST /musiclife/user/add` : This will register a new user.

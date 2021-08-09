import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.movie_info import (
    add_review,
    get_reviews_from_album,
    get_list_albums,
    get_list_artists,
    update_album_details
)

app = BottleJson()

@app.get("/")
    #Default route

## Get albums list
## Curl example:
# curl http://localhost:8080/movie/list -X GET
@app.get("/list")
def get_all_albums(*args, **kwargs):
    try:
       respuesta = get_list_albums()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Get artists list
## Curl example:
# curl http://localhost:8080/movie/list -X GET
@app.get("/list")
def get_all_artists(*args, **kwargs):
    try:
       respuesta = get_list_artists()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Update movie details
## This works as a simple post. The store_string function
## updates de info that was previously storaged.
## Curl example to update the Soy Leyenda movie information
## curl http://localhost:8080/movie/M002 -X POST -H /
##'Content-Type: application/json' -d /
##'{"movie_id": "M002","title": "Soy Leyenda", "genre2": "Accion", "director": "Francis Lawrence", "release_date": "2008-01-18", "sinopsys": "Un cientifico lucha por sobrevivir contra unos mutantes nocturnos con sed de sangre."}'
@app.post("/<movie_id>")
def update_album_details(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_artist = str(payload['id_artist'])
        review_id = str(payload['review_id'])
        user_id = str(payload['user_id'])
        album_id = str(payload['album_id'])
        rate = str(payload['rate'])
        comment = str(payload['comment'])
        print("Datos validos")
        respuesta = update_album_details(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, "Movie data has been updated")

## Add a review to a certain album
# Example curl:
# curl http://localhost:8080/movie/007/review -X POST -H 'Content-Type: application/json' -d '{"review_id": "002","user_id": "001", "movie_id": "007", "movie_title": "Inception", "rate": "5", "comment": "goooood bro ngl"}'
@app.post("/<movie_id>/review")
def bar(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id_artist = str(payload['id_artist'])
        review_id = str(payload['review_id'])
        user_id = str(payload['user_id'])
        album_id = str(payload['album_id'])
        rate = str(payload['rate'])
        comment = str(payload['comment'])
        print("Datos validos")
        respuesta = add_review(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, "Your review has been succesfully added")

## Get all reviews from a movie
## Curl example:
# curl http://localhost:8080/movie/M001/reviews -X GET
@app.get("/<movie_id>/reviews")
def get_all_reviews_from_movie(*args, album_id=None, **kwargs):
    try:
       respuesta = get_reviews_from_album(album_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

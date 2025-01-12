import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.musiclife import (
    add_review,
    get_reviews_from_album,
    get_list_albums,
    get_list_artists,
    update_album_details
)

app = BottleJson()

## Get albums list
## Curl example:
@app.get("/list")
def get_all_albums(*args, **kwargs):
    try:
       respuesta = get_list_albums()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Get artists list
## Curl example:
@app.get("/list")
def get_all_artists(*args, **kwargs):
    try:
       respuesta = get_list_artists()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Update albums details
## This works as a simple post. The store_string function
## updates de info that was previously storaged.
@app.post("/<musiclife>")
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
    raise bottle.HTTPError(201, "Album data has been updated")

## Add a review to a certain album
@app.post("/<musiclife>/review")
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

## Get all reviews from an album
@app.get("/<musiclife>/reviews")
def get_all_reviews_from_album(*args, album_id=None, **kwargs):
    try:
       respuesta = get_reviews_from_album(album_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

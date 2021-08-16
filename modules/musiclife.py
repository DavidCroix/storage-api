import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)
def add_review(review_id = None, user_id = None, album_id = None, id_artist = None, rate = None, comment = None):
    print("Desde Modulo add_review")
    print(review_id, user_id, album_id, rate, comment)
    print("Good")

    almacenable = {
        "review_id": review_id,
        "user_id": user_id,
        "album_id": album_id,
        "id_artist": id_artist,
        "rate": rate,
        "comment": comment,
    }
    nombre_de_archivo = f"{album_id}-{review_id}-{id_artist}.json"
    datos = store_string(
        "album/reviews",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_reviews_from_album(album_id = None, reviews = None):
    query_result = query_storage(
        "album/reviews",
    )
    if album_id is not None:
        return [
           r
           for r in query_result["content"]
           if album_id in r
        ]
    print("Conejo Blas")

def get_list_albums(albums=None):
    query_result = query_storage(
        "album/albums",
    )
    if albums is None:
        return query_result["content"]

def get_list_artists(artists=None):
    query_result = query_storage(
        "artist/artists",
    )
    if albums is None:
        return query_result["content"]

def update_album_details(review_id = None, user_id = None, album_id = None, id_artist = None, rate = None, comment = None ):
    print("Desde Modulo store")
    print(review_id, user_id, album_id, rate, comment)
    print("Good")

    almacenable = {
        "review_id": review_id,
        "user_id": user_id,
        "album_id": album_id,
        "id_artist": id_artist,
        "rate": rate,
        "comment": comment,
    }
    nombre_de_archivo = f"{album_id}-{id_artist}.json"
    datos = store_string(
        "album/albums",
        nombre_de_archivo,
        json.dumps(almacenable),
        update=True
    )
    return datos



## Extension para ver si funciona

## add_album
def add_album(id_artist = None, album_id = None, genre = None):

    print("Desde Modulo add_album")
    print(id_artist, album_id, genre)
    print("Exito")

    almacenable = {
        "id_artist": id_artist,
        "album_id": album_id,
        "genre": genre,
    }
    nombre_de_archivo = f"{id_artist}-{album_id}.json"
    datos_album = store_string(
        "album/albums",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos_album

def add_artist(id_artist = None, genre = None):

	print("Desde Modulo add_artist")
    print(id_artist, genre)
    print("Exito")

	almacenable = {
        "id_artist": id_artist,
        "genre": genre,
	}
	nombre_de_archivo = f"{id_artist}.json"
    datos_artist = store_string(
        "artist/artists",
        nombre_de_archivo,
        json.dumps(almacenable)
    )

    return datos_artist

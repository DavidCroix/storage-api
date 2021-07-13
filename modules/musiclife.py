import datetime
import binascii
from functools import wraps
from os import environ, urandom
import hashlib
from bottle import response, request
import jwt
import models.auth as mauth

comments= []
def add_comment(artist_id, album_id, rate):
    comment = {
        "album_id": artist_id,
        "album_id": album_id,
        "rate": rate,
        "user_id": user_id
    }
    comments.append(comment)
    return json.dumps(comment)

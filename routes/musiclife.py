from json import dumps as json_dumps
from os import environ
import bottle
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required

app = bottle.Bottle()

## Get the login
@app.get("/musiclife/login")
def get_artist_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get the artist list
@app.get("/musiclife/artists_list")
def get_artist_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get the artist albums
@app.post("/musiclife/albums_lists_artist")
def get_artist_albums(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add a user
@app.get("/musiclife/user/add")
def add_a_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get the complete list of albums
@app.post("/musiclife/albums")
def get_all_albums(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

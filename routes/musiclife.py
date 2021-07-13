from json import dumps as json_dumps
from os import environ
import bottle
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required

app = bottle.Bottle()

## Get artist list
@app.get("/musiclife/list")
def get_artist_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get artist details
@app.get("/musiclife/<artist_id>")
def get_artist_details(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Update artist details
@app.post("/musiclife/<artist_id>")
def update_artist_details(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get all reviews from an artist
@app.get("/musiclife/<artist_id>/review")
def get_all_artist_reviews(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add a review to a certain album
@app.post("/musiclife/<artist_id>/review")
def add_a_review(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get a certain review from a certain artist
@app.get("/musiclife/<artist_id>/review/<review_id>")
def get_review_from_artist(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

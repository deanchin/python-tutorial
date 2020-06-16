""" Movies Endpoint """
from flask import request
from flask_restx import Namespace, Resource, fields

from service.movies import Movies

NS = Namespace(
    'movies',
    description='Operations related to movies'
)

MOVIE = NS.model(
    "Item", {
        "name": fields.String(
            required=True,
            description="Movie name",
            example="Movie Name"
        ),
        "genre": fields.String(
            required=True,
            description="Genre",
            example="Genre",
            pattern=r'^[A-Z]{1}[a-z]+$'
        ),
        "phone": fields.String(
            required=True,
            description="Phone number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "inTheaters": fields.Boolean(
            default=False,
            description="Is the movie showing in the theaters"
        )
    }
)

PUT_MOVIE = NS.model(
    "Item", {
        "name": fields.String(
            description="Movie name",
            example="Movie Name"
        ),
        "genre": fields.String(
            description="Genre",
            example="Genre",
            pattern=r'^[A-Z]{1}[a-z]+$'
        ),
        "phone": fields.String(
            description="Phone number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        ),
        "inTheaters": fields.Boolean(
            default=False,
            description="Is the movie showing in the theaters"
        )
    }
)


@NS.route("")
class MoviesCollection(Resource):
    """ Movies Collection methods """

    def get(self):
        """ Returns list of movies """
        return Movies().get_all()

    @NS.expect(MOVIE, validate=True)
    def post(self):
        """ Adds a new movie """
        return Movies().create_one(request.get_json())


@NS.route("/<string:name>")
class MovieItem(Resource):
    """ Movie methods """

    def get(self, name):
        """ Returns a movie with name """
        return Movies().get_one(name)

    @NS.expect(PUT_MOVIE, validate=True)
    def put(self, name):
        """ Updates a movie with name """
        return Movies().update_one(name, request.json)

    def delete(self, name):
        """ Deletes a movie with name """
        return Movies().delete_one(name)

""" Items Endpoint """
from flask import request
from flask_restx import Namespace, Resource

from service.items import Items

NS = Namespace(
    'items',
    description='Operations related to items'
)

@NS.route("")
class ItemsCollection(Resource):
    """ Items Collection methods """

    def get(self):
        """ Returns list of items """
        return Items().get_all()

    def post(self):
        """ Creates a new item """
        return {'message': 'Created Item'}, 201


@NS.route("/<string:name>")
class Item(Resource):
    """ Item methods """

    def get(self, name):
        """ Returns a item with name """
        return Items().get_one(name)

    def put(self, name):
        """ updates a item with name """
        return Items().update_one(name, request.json)

    def delete(self, name):
        """ deletes a item with name """
        return Items().delete_one(name)

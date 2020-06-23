""" Contacts Endpoint """
from flask import request
from flask_restx import Namespace, Resource, fields, inputs, reqparse

from service.contacts import Contacts

NS = Namespace(
    'contacts',
    description='Operations related to contacts'
)

# localhost:5000/movies?genre=value1&inTheathers=value2&fields=[name,address]
GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    'firstName',
    required=False, default=None,
    help='First Name')
GET_PARSER.add_argument(
    'lastName',
    required=False, default=None,
    help='Last Name')

CONTACT = NS.model(
    "Item", {
        "firstName": fields.String(
            required=True,
            description="First name",
            example="First Name"
        ),
        "lastName": fields.String(
            required=True,
            description="Last name",
            example="Last Name"
        ),
        "address": fields.String(
            required=True,
            description="address",
            example="Address"
        ),
        "phone": fields.String(
            required=True,
            description="Phone number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        )
    }
)

PUT_CONTACT = NS.model(
    "Item", {
        "firstName": fields.String(
            required=True,
            description="First name",
            example="First Name"
        ),
        "lastName": fields.String(
            required=True,
            description="Last name",
            example="Last Name"
        ),
        "address": fields.String(
            required=True,
            description="address",
            example="Address"
        ),
        "phone": fields.String(
            required=True,
            description="Phone number",
            example="000-000-0000",
            pattern=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
        )
    }
)


@NS.route("")
class ContactsCollection(Resource):
    """ Contacts Collection methods """

    @NS.doc(parser=GET_PARSER)
    def get(self):
        """ Returns list of movies """
        args = GET_PARSER.parse_args()
        print(f'args={args}')
        return Contacts().get_all(args['firstName'], args['lastName'])

    @NS.expect(CONTACT, validate=True)
    def post(self):
        """ Adds a new movie """
        return Contacts().create_one(request.get_json())


@NS.route("/<string:name>")
class ContactItem(Resource):
    """ Movie methods """

    def get(self, name):
        """ Returns a movie with name """
        return Contacts().get_one(name)

    @NS.expect(PUT_CONTACT, validate=True)
    def put(self, name):
        """ Updates a movie with name """
        return Contacts().update_one(name, request.json)

    def delete(self, name):
        """ Deletes a movie with name """
        return Contacts().delete_one(name)

''' Application Entrypoint '''
from flask import Flask
from flask_restx import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

@api.route('/hello')
class HelloWorld(Resource):
    @auth.login_required
    def get(self):
        return {'hello': 'world'}


    @auth.verify_password
    def verify_password(username, password):
        print(f'Checking {username}:{password}')
        if username == 'dean':
            return True
        if password == 'something':
            return True
        return False


@api.route('/wassup')
class wassup(Resource):
    def get(self):
        return {'wassup': 'there'}

# @api.route('/api/resource')
# @auth.login_required
# def get_resource():
#     return {'data': 'Hello, Dean!'}, 200

# @auth.verify_password
# def verify_password(username, password):
#     return True


if __name__ == '__main__':
    app.run(debug=True)






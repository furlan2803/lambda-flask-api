from flask import Flask, request
import base64
import json
import pprint

app = Flask(__name__)

class LambdaHandler:
    def __init(self, users):
        self.users = users

    def authenticate_user(self, request):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header or not authorization_header.startswith('Basic '):
            return False

        encoded_credentials = authorization_header[len('Basic '):]
        credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        username, password = credentials.split(':')

        return self.users.get(username) == password

    def get_resource(self):
        if self.authenticate_user(request):
            input_json = json.loads(request.data)
            formatted_json = pprint.pformat(input_json)
            return formatted_json
        return "Acesso não autorizado", 401

    def create_resource(self):
        if self.authenticate_user(request):
            return "POST resource"
        return "Acesso não autorizado", 401

users = {
    "Giovanna": "AlunoLambdaFlask",
    "Afonso": "ProfessorLambdaFlask",
}

lambda_handler = LambdaHandler(users)

@app.route('/api/resource', methods=['GET'])
def get_resource_route():
    return lambda_handler.get_resource()

@app.route('/api/resource', methods=['POST'])
def create_resource_route():
    return lambda_handler.create_resource()

if __name__ == '__main__':
    app.run()

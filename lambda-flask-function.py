import base64
import json
import pprint

users = {
    "Giovanna": "AlunoLambdaFlask",
    "Afonso": "ProfessorLambdaFlask",
}

def authenticate_user(event):
    headers = event.get('headers', {})
    authorization_header = headers.get('Authorization', '')

    if not authorization_header:
        return False

    if authorization_header.startswith('Basic '):
        encoded_credentials = authorization_header[len('Basic '):]
        credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        user, password = credentials.split(':')

        if user in users and users[user] == password:
            return True

    return False

def lambda_handler(event, context):
    if authenticate_user(event):
        try:
            input_json = json.loads(event['body'])
            formatted_json = pprint.pformat(input_json)
            return {
                'statusCode': 200,
                'body': formatted_json
            }
        except json.JSONDecodeError as e:
            return {
                'statusCode': 400,
                'body': f'Erro na decodificação JSON: {str(e)}'
            }
    else:
        return {
            'statusCode': 401,
            'body': 'Acesso não autorizado'
        }
import unittest
from lambda_function.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_successful_authentication(self):
        # Testa a autenticação bem-sucedida e corpo com JSON válido
        response = self.app.get('/default/lambda-flask-function?auth=Afonso:ProfessorLambdaFlask', data='{"key": "value"}')
        self.assertEqual(response.status_code, 200)

    def test_failed_authentication(self):
        response = self.app.get('/default/lambda-flask-function?auth=usuario_inexistente:senha_incorreta', data='{"key": "value"}')
        self.assertEqual(response.status_code, 401)  # 401 Unauthorized - Autenticação falhou

    def test_unauthorized_access(self):
        # Testa evento sem autenticação
        response = self.app.get('/default/lambda-flask-function', data='{"key": "value"}')
        self.assertEqual(response.status_code, 401)  # 401 Unauthorized - Acesso não autorizado

    def test_lambda_function_works(self):
        # Teste para verificar se o Lambda está funcionando
        response = self.app.get('/default/lambda-flask-function', data='{"key": "value"}')
        self.assertEqual(response.status_code, 200)

    def test_successful_authentication_empty_body(self):
        # Teste com autenticação bem-sucedida e corpo vazio
        response = self.app.get('/default/lambda-flask-function?auth=Afonso:ProfessorLambdaFlask', data='{}')
        self.assertEqual(response.status_code, 200)

    def test_successful_authentication_multiple_fields(self):
        # Teste com autenticação bem-sucedida e corpo com múltiplos campos
        data = '[ {"name": "Harry Potter","species": "human","gender": "male","house": "Gryffindor","dateOfBirth": "31-07-1980","yearOfBirth": 1980,"ancestry": "half-blood","eyeColour": "green","hairColour": "black","wand": {"wood": "holly","core": "phoenix feather","length": 11},]'
        response = self.app.get('/default/lambda-flask-function?auth=Giovanna:AlunoLambdaFlask', data=data)
        self.assertEqual(response.status_code, 200)

    def test_authentication_missing_url_and_valid_body(self):
        # Teste com autenticação ausente na URL e corpo com dados válidos
        response = self.app.get('/default/lambda-flask-function', data='{"key": "value"}')
        self.assertEqual(response.status_code, 401)  # 401 Unauthorized - Acesso não autorizado

if __name__ == '__main__':
    unittest.main()

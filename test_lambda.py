import json

def autenticacao_bem_sucedida(event):
    query_params = event.get("queryStringParameters")
    if query_params and "auth" in query_params:
        auth_param = query_params["auth"]
        if auth_param == "Afonso:ProfessorLambdaFlask":
            body = json.loads(event.get("body"))
            return "Autenticação bem-sucedida"
    
    return "Acesso não autorizado"

def autenticacao_malsucedida(event):
    query_params = event.get("queryStringParameters")
    if query_params and "auth" in query_params:
        auth_param = query_params["auth"]
        if auth_param != "Afonso:ProfessorLambdaFlask":
            body = json.loads(event.get("body"))
            return "Autenticação malsucedida"
    
    return "Acesso não autorizado"

def evento_sem_autenticacao(event):
    query_params = event.get("queryStringParameters")
    if not query_params or "auth" not in query_params:
        body = json.loads(event.get("body"))
        return "Acesso não autorizado"
    
    return "Acesso autorizado"


def autenticacao_e_verificacao_json(event):
    query_params = event.get("queryStringParameters")
    if query_params and "auth" in query_params:
        auth_param = query_params["auth"]
        if auth_param == "Afonso:ProfessorLambdaFlask":
            body = event.get("body")
            if not body:
                return "Autenticação bem-sucedida, mas JSON vazio"
            try:
                body_dict = json.loads(body)
                if isinstance(body_dict, dict):
                    return "Autenticação bem-sucedida e JSON formatado corretamente"
                else:
                    return "Autenticação bem-sucedida, mas o JSON não está formatado corretamente"
            except json.JSONDecodeError:
                return "Autenticação bem-sucedida, mas o JSON não está formatado corretamente"
    
    return "Acesso não autorizado"



event1 = {
    "queryStringParameters": { "auth": "Afonso:ProfessorLambdaFlask" },
    "body": "{\"key\": \"value\"}"
}

event2 = {
    "queryStringParameters": { "auth": "usuario_inexistente:senha_incorreta" },
    "body": "{\"key\": \"value\"}"
}

event3 = {
    "queryStringParameters": {},
    "body": "{\"key\": \"value\"}"
}

event4 = {
    "queryStringParameters": { "auth": "Afonso:ProfessorLambdaFlask" },
    "body": "{name: \"Alice\", age: 25, email: \"alice@example.com\"}"
}

event5 = {
    "queryStringParameters": { "auth": "Afonso:ProfessorLambdaFlask" },
    "body": "{\"name\": \"Alice\", \"age\": 25, \"email\": \"alice@example.com\"}"
}

print('\n\nTeste 1 - Evento de autenticação com credêncial válida : Resultado do teste - ' + autenticacao_bem_sucedida(event1) + '\n')
print('Teste 2 - Evento de autenticação con credêncial inválida : Resultado do teste - ' + autenticacao_malsucedida(event2) + '\n')
print('Teste 3 - Evento sem autenticação : Resultado do teste - ' + evento_sem_autenticacao(event3) + '\n')
print('Teste 4 - Json mal formatado : Resultado do teste - ' + autenticacao_e_verificacao_json(event4) + '\n')
print('Teste 5 - Json com formato adequado : Resultado do teste - ' + autenticacao_e_verificacao_json(event5) + '\n\n')

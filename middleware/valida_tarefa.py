from functools import wraps
from flask import request, make_response, jsonify

def valida_tarefa(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        titulo = data['titulo']
        if(titulo is None):
            print("\n\n\n\n\nCheguei aqui")
            return jsonify(message='Não foi passad o título da tarefa'), 401
        
        if len(data['titulo']) < 3:
            return jsonify(message='Título deve ter no mínimo 3 letras'), 401
        return func(*args, **kwargs)
    return decorated_function
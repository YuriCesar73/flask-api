from functools import wraps
from flask import request, make_response, jsonify

def valida_tarefa(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        if len(data['titulo']) < 3:
            return make_response(jsonify(message='Título deve ter no mínimo 3 letras'), 401)
        return func(*args, **kwargs)
    return decorated_function
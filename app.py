from flask import Flask, make_response, jsonify, request
from db import db
from flask_migrate import Migrate
from models.tarefa import Tarefa

app = Flask(__name__)
app.json.sort_keys = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yuri:929305@localhost/tarefas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/tarefa', methods=['GET'])
def get_tarefas():
    tarefas = Tarefa.query.all()
    return make_response(
        jsonify([tarefa.as_dict() for tarefa in tarefas])
    ) 

@app.route('/tarefa', methods=['POST'])
def create_tarefa():
    data = request.get_json()
    novaTarefa = Tarefa(titulo=data['titulo'], descricao=data['descricao'], )
    db.session.add(novaTarefa)
    db.session.commit()
    return make_response(
        jsonify(
            message='Tarefa criada com sucesso',
            data=novaTarefa.as_dict()
        ),
        201
    )

@app.route('/tarefa/<int:id>', methods=['GET'])
def get_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    return jsonify(tarefa.as_dict())

@app.route('/tarefa/<int:id>', methods=['PUT'])
def update_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
            setattr(tarefa, key, value)
    db.session.commit()
    return jsonify({'message': 'Tarefa atualizada com sucesso!'})

@app.route('/tarefa/<int:id>', methods=['DELETE'])
def delete_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'message': 'Tarefa removida com sucesso!'})



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, make_response, jsonify, request
from db import db
from flask_migrate import Migrate
from models.tarefa import Tarefa
from middleware.valida_tarefa import valida_tarefa
from datetime import datetime


app = Flask(__name__)
app.json.sort_keys = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yuri:929305@localhost/tarefas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/tarefa', methods=['GET'])
def get_tarefas():
    try:
        tarefas = Tarefa.query.all()
        return make_response(
            jsonify([tarefa.as_dict() for tarefa in tarefas])
        )
    except:
         return make_response(
              jsonify(
                   message='Ocorreu um erro'
              ), 
              400
         ) 


@app.route('/tarefa', methods=['POST'])
@valida_tarefa
def create_tarefa():
    try:
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
    except:
         return make_response(jsonify(message='Ocorreu um erro'), 400)

@app.route('/tarefa/<int:id>', methods=['GET'])
def get_tarefa(id):
    try:
        tarefa = Tarefa.query.get_or_404(id)
        return jsonify(tarefa.as_dict())
    except:
         return make_response(
              jsonify(
                   message="Não existe tarefa com o id: {}" .format(id)
              ),
              404
         )

@app.route('/tarefa/<int:id>', methods=['PUT'])
def update_tarefa(id):
    try:
        tarefa:Tarefa = Tarefa.query.get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
                setattr(tarefa, key, value)
        tarefa.date_updated = datetime.utcnow()
        db.session.commit()
        return make_response(
            jsonify(
            {'message': 'Tarefa atualizada com sucesso!', 'data': tarefa.as_dict()}
            ),
            200 
        ) 
    except:
        return make_response(
            jsonify(message='Não existe tarefa com id: {}'.format(id)),
            404
        )

@app.route('/tarefa/<int:id>', methods=['DELETE'])
def delete_tarefa(id):
    try:
        tarefa = Tarefa.query.get_or_404(id)
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa removida com sucesso!'})
    except:
      return make_response(
          jsonify(
              message="Não existe tarefa com id: {}".format(id)
          ),
          404
      )   


if __name__ == '__main__':
    app.run(debug=True)
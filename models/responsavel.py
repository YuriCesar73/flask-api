from db import db
from datetime import datetime

class Responsavel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    is_ativo = db.Column(db.Boolean, default=False)
    tarefas = db.relationship('Tarefa', backref='responsavel', lazy=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)


    def as_dict(self):
        return {
            'id': str(self.id),
            'nome': self.nome,
            'email': self.email,
            'isAtivo': str(self.is_ativo),
            'tarefas': self.__tarefas_responsavel(),
            'date_created': str(self.date_created),
            'date_updated': str(self.date_updated)
        }
    
    def __tarefas_responsavel(self):
        dados = []
        for tarefa in self.tarefas:
            dados.append(tarefa.as_dict())

        return dados

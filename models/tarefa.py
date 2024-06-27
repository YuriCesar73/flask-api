from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy import func
from db import db
from datetime import datetime

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(TEXT(), nullable=False)
    isFavorito = db.Column(db.Boolean, default=False)
    isFinalizado = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def as_dict(self):
        return {
            'id': str(self.id),
            'titulo': self.titulo,
            'descricao': self.descricao,
            'isFavorito': str(self.isFavorito),
            'isFinalizado': str(self.isFinalizado),
            'date_created': str(self.date_created)
        }

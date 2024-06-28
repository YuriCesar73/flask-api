from sqlalchemy.dialects.postgresql import TEXT
from db import db
from datetime import datetime

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(TEXT(), nullable=False)
    isFavorito = db.Column(db.Boolean, default=False)
    isFinalizado = db.Column(db.Boolean, default=False)
    responsavel_id = db.Column(db.Integer, db.ForeignKey('responsavel.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)


    def as_dict(self):
        return {
            'id': str(self.id),
            'titulo': self.titulo,
            'descricao': self.descricao,
            'isFavorito': str(self.isFavorito),
            'isFinalizado': str(self.isFinalizado),
            'responsavel': str(self.responsavel_id),
            'date_created': str(self.date_created),
            'date_updated': str(self.date_updated)
        }

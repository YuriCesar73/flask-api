from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://yuri:929305@localhost/tarefas'
db = SQLAlchemy()



#CRIA O BANCO DE DADOS
# def create_database():
#     with app.app_context():
#         db.create_all() 

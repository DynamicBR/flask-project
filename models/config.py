from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configurar_banco(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja_alunos.db'
    app.secret_key = 'aula_flask_123' 
    db.init_app(app)
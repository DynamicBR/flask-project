from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configurar_banco(app):
    # Conexão com o MySQL usando pymysql na porta padrão 3306
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dM!TR!1001@localhost:3306/loja'
    
    app.secret_key = 'aula_flask_123' 
    db.init_app(app)
import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from apps.authentication import auth
from apps.admin import admin
from apps.users import user
from apps.coverage import register


# Instância da aplicação e banco de dados
app = Flask(__name__)
db = SQLAlchemy()


# Diretório raíz do projeto
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Diretório do banco de dados do projeto
database_path = os.path.join(root_path, 'database', 'Tavellas.db')
# Diretório das pastas da aplicação
template_path = os.path.join(root_path, 'templates')
static_path = os.path.join(root_path, 'static')


# Configurações da aplicação
app.template_folder = template_path
app.static_folder = static_path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SECRET_KEY'] = 'FATEC&FLAMENGO=DUAS_COISAS_QUE_ME_CAUSAM_DOR'

# Inicialização do banco (método útil para aplicações modulares)
db.init_app(app) 


# Registrando as rotas
app.register_blueprint(admin, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(register, url_prefix="/register")


# > TMP: Criar o arquivo .db e/ou tabelas
# with app.app_context():
    # db.create_all()
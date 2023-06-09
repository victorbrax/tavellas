import os

basedir = os.path.abspath(os.path.dirname(__file__))

class DevConfig:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7d2e8a1b3f9c6e5d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class QasConfig:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or ' 7d2e8a1b3f9c6e5d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
#! Objeto de Configuração de Exemplo
from datetime import timedelta
class PrdConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7d2e8a1b3f9c6e5d'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
 
    # Configurações de e-mail
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your-email@example.com'
    MAIL_PASSWORD = 'your-email-password'

    # Configurações de armazenamento de arquivos (por exemplo, para upload de arquivos)
    UPLOAD_FOLDER = '/path/to/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    # Configurações de autenticação
    JWT_SECRET_KEY = 'supersecretkey'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    # Configurações de cache
    CACHE_TYPE = 'simple'  # ou 'redis', 'memcached', etc.
    CACHE_DEFAULT_TIMEOUT = 3600  # tempo de expiração em segundos

    # Configurações de internacionalização (tradução)
    BABEL_DEFAULT_LOCALE = 'pt_BR'

    # Configurações de logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = '/path/to/app.log'

    # Configurações de segurança
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
from flask import Flask

from config import DevConfig
from app.extensions import db

def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)

    # Blueprint Registers
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.register import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/registrar')

    return app
from apps.authentication import auth
from apps.admin import admin
from apps.users import user
from apps.coverage import register


def register_blueprints(app):

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(register, url_prefix="/register")
    
    return app
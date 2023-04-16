from apps.authentication import auth
from apps.admin import admin
from apps.users import user


def register_blueprints(app):

    app.register_blueprint(auth, url_prefix="/login")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(admin, url_prefix="/admin")
    
    return app
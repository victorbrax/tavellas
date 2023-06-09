from flask import render_template
from app.auth import bp


@bp.route('/login')
def index():
    return render_template('auth/index.html', 
                           inspiration_image='wallpaper1')

@bp.route('/cadastrar')
def register():
    return render_template('auth/register.html', 
                           inspiration_image='wallpaper2')

@bp.route('/esqueceu_senha')
def forgot():
    return render_template('auth/forgot.html', 
                           inspiration_image='wallpaper3')

@bp.route('/trocar_senha')
def change():
    return render_template('auth/change.html', 
                           inspiration_image='wallpaper3')

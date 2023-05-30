from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, static_folder="static", template_folder="templates")

@auth.route('/login')
def auth_page():
    return render_template('accounts/login.html', 
                           inspiration_image='wallpaper1')

@auth.route('/cadastrar')
def access_page():
    return render_template('accounts/access.html', 
                           inspiration_image='wallpaper2')

@auth.route('/esqueceu_senha')
def forgot_page():
    return render_template('accounts/forgot_pass.html', 
                           inspiration_image='wallpaper3')

# Criar essa página e adicionar wallpaper de inspiração
@auth.route('/trocar_senha')
def change_page():
    return render_template('accounts/change_pass.html', 
                           inspiration_image='wallpaper3')


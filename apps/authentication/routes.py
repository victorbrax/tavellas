from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, static_folder="static", template_folder="templates")

@auth.route('/login')
def auth_page():
    return render_template('accounts/login.html', 
                           inspiration_image='wallpaper1')

@auth.route('/register')
def register_page():
    return render_template('accounts/register.html', 
                           inspiration_image='wallpaper2')

@auth.route('/forgot')
def forgot_page():
    return render_template('accounts/forgot_pass.html', 
                           inspiration_image='wallpaper3')
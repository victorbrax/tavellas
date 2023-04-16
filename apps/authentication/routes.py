from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, static_folder="static", template_folder="templates")

@auth.route('/')
def auth_page():
    return render_template('accounts/login.html')
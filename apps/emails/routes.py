from flask import Blueprint, render_template

emails = Blueprint('user', __name__, static_folder="static", template_folder="templates")


@emails.route('/suporte')
def suport():
    return render_template('emails/support.html')
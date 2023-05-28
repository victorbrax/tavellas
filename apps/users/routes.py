from flask import Blueprint, render_template

user = Blueprint('user', __name__, static_folder="static", template_folder="templates")

@user.route('/')
def user_page():
    return render_template('user/user.html')

@user.route('/suporte')
def user_suport():
    return render_template('user/suporte.html')

@user.route('/demandas')
def user_demands():
    return render_template('user/demandas.html', aguardando  = {}, 
                                                 emReparo    = {}, 
                                                 finalizadas = {}, 
                                                 entregues   = {})
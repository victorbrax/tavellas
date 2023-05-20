from flask import Blueprint, render_template

register = Blueprint('register', __name__, static_folder="static", template_folder="templates")

@register.route('/clientes')
def register_clients():
    return render_template('coverage/register_client.html')

@register.route('/servicos')
def register_services():
    return render_template('coverage/register_service.html')

@register.route('/magrelas')
def register_bikes():
    return render_template('coverage/register_bike.html')

@register.route('/bikeclass')
def register_bike_class():
    return render_template('coverage/register_bike_class.html')

@register.route('/produtos')
def register_products():
    return render_template('coverage/register_product.html')

@register.route('/usuarios')
def register_users():
    return render_template('coverage/register_user.html')

@register.route('/cargos')
def register_cargos():
    return render_template('coverage/register_cargo.html')


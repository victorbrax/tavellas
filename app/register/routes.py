from flask import render_template
from app.register import bp


@bp.route('/')
def index():
    return render_template('register/index.html')

@bp.route('/clientes')
def register_clients():
    return render_template('register/client.html')

@bp.route('/servicos')
def register_services():
    return render_template('register/service.html')

@bp.route('/magrelas')
def register_bikes():
    return render_template('register/bike.html')

@bp.route('/classe')
def register_bike_class():
    return render_template('register/class.html')

@bp.route('/produtos')
def register_product():
    return render_template('register/product.html')

@bp.route('/tipoprodutos')
def register_product_type():
    return render_template('register/product_type.html')

@bp.route('/usuarios')
def register_users():
    return render_template('register/user.html')

@bp.route('/cargos')
def register_cargos():
    return render_template('register/job.html')


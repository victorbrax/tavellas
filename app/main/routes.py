from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    return render_template("main/index.html")

@bp.route('/demandas')
def demands():
    return render_template("main/demands.html")

# Criar o Modal de Serviços
@bp.route('/tmpdemands')
def tmpdemands():
    return render_template("main/service_modal.html.html")
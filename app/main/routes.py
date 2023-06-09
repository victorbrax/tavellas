from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    return render_template("main/index.html")

@bp.route('/demandas')
def demands():
    return render_template("main/demands.html")
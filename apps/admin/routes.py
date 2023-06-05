from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder="static", template_folder="templates")

@admin.route('/home')
@admin.route('/')
def home_page():
    return render_template('admin/index.html')

@admin.route('/demandas')
def demands_page():
    return render_template('admin/demands.html')
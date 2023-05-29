from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder="static", template_folder="templates")

@admin.route('/home')
def home_page():
    return render_template('admin/admin.html')

@admin.route('/newbase')
def newbase():
    return render_template('admin/newbase.html')
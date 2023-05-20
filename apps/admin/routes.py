from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder="static", template_folder="templates")

@admin.route('/sidebar')
def sidebar_page():
    return render_template('layouts/sidebar.html')



from app import app
from flask import render_template
from app.models import Models

@app.route('/admin/table/')
def admin_table():
    database = Models()
    query = database.Select_Data()
    return render_template('admin/admin.html', datas = query['data'])

@app.route('/admin/login/')
def admin_login():
    return render_template('admin/login.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
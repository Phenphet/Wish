from app import app
from flask import render_template
from app.models import Models

@app.route('/admin/')
def admin():
    database = Models()
    query = database.Select_Data()
    return render_template('admin/admin.html', datas = query['data'])

@app.route('/admin/login/')
def login():
    return render_template('admin/login.html')
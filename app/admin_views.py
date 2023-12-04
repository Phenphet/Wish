from app import app
from flask import render_template, request, jsonify
from app.models import Models

@app.route('/wish/admin/table', methods=['GET', 'POST'])
def admin_table():
    database = Models()
    query = database.Select_Data()
    if request.method == 'POST':
        try:
            data = request.form.get('id')
            database.Delete_Data(data)
            return jsonify({'success' : 'ลบข้อมูลเรียบร้อย'})
        except Exception as ex:
            return jsonify({'error' : ex})
    return render_template('admin/admin.html', datas = query['data'])

@app.route('/wish/admin/login/', methods=['GET','POST'])
def admin_login():
    return render_template('admin/login.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
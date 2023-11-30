from app import app
from app.models import Models
from app.check_text_wish import CheckText
from flask import request, jsonify, render_template

@app.route('/wish/', methods=['GET'])
def home():
    try:
        database = Models()
        query = database.Select_Data()
        return render_template('page/home.html', data=query['data'])
    except Exception as ex:
        return f'error {ex}'

@app.route('/wish/form/ldo/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            form_darta = request.form
            if form_darta.get('fullname') == '' or form_darta.get('wish') == '':
                return jsonify({'error': 'ตรวจพบว่าคุณยังกรอกข้อมูลไม่ครบ'})
            elif form_darta.get('fullname').count(' ') > 2:
                return jsonify({'error': 'ตรวจพบข้อผิดพลาดกรุณาลองใหม่อีกครั้ง'})
            else:
                test = CheckText()
                count, listtext = test.Check(form_darta.get('wish'))
                if count > 0:
                    return jsonify({'error': 'ตรวจพบคำหยาบในคำอวยพรของคุณกรุณาตรวจสอบข้อความที่พิมพ์มาด้วย', 'data': listtext})
                else:
                    database = Models()
                    database_massage = database.Insert_Data(form_darta)
                    if database_massage == 'success':
                        return jsonify({database_massage : 'บันทึกข้อมูลเรียบร้อยเเล้ว'})
                    else:
                        return jsonify({'error': f'{database_massage}'})
        except Exception as ex:
            return jsonify({'error': f'ตรวจพบข้อผิดพลาด : {ex}'})
    return render_template('page/form.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
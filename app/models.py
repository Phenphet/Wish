from app import db
import sqlite3
import datetime

new_time = datetime.datetime.now()

class Models:
    def __init__(self, database_path=db):
        self.db = database_path
        self.migation_table()

    def GenerateConect(self) -> str:
        connect = sqlite3.connect(self.db)
        return connect
    
    def migation_table(self) -> None: 
        connect = self.GenerateConect()
        cursor = connect.cursor()
        query = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" and name="tbl_wish"').fetchall()
        if len(query) == 0:
            cursor.execute("""
                CREATE TABLE tbl_wish (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    fullname VARCHAR(100), 
                    wish VARCHAR(255),
                    department VARCHAR(100),
                    company VARCHAR(150), 
                    created DATETIME DEFAULT CURRENT_TIMESTAMP 
                );
            """)
            connect.commit()

    def Select_Data(self) -> dict: 
        try:
            connect = self.GenerateConect()
            cursor = connect.cursor()
            query = cursor.execute('SELECT * FROM tbl_wish ORDER BY id DESC').fetchall()
            datas = []
            for data in query:
                row = {
                    'id': data[0],
                    'fullname': data[1],
                    'wish': data[2],
                    'department': data[3],
                    'company' : data[4],
                    'time' : data[5]
                }
                datas.append(row)
            return {'data' : datas}
        except Exception as ex:
            return {'error' : ex}

    def Insert_Data(self, data: dict) -> str:
        try:   
            connect = self.GenerateConect()
            cursor = connect.cursor()
            cursor.execute("INSERT INTO tbl_wish (fullname, wish, department, company) VALUES('" + data['fullname'] + "','" + data['wish'] + "','" + data['department'] + "','" + data['company'] + "');")
            connect.commit()
            return 'success'
        except Exception as ex:
            return str(ex)
        
    def Delete_Data(self, Id_Data: int):
        try:
            connect = self.GenerateConect()
            cursor = connect.cursor()
            cursor.execute("DELETE FROM tbl_wish WHERE id = " + Id_Data + ";")
            connect.commit()
            print('complete')
        except Exception as ex:
            return str(ex)
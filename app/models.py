from app import db
import sqlite3

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
                    created DATETIME DEFAULT CURRENT_TIMESTAMP 
                )
            """)
            connect.commit()

    def Select_Data(self) -> dict: 
        try:
            connect = self.GenerateConect()
            cursor = connect.cursor()
            query = cursor.execute('SELECT * FROM tbl_wish ').fetchall()
            datas = []
            for data in query:
                row = {
                    'id': data[0],
                    'fullname': data[1],
                    'wish': data[2],
                    'time': data[3]
                }
                datas.append(row)
            return {'data':datas}
        except Exception as ex:
            return {'error' : ex}

    def Insert_Data(self, data: dict) -> None:
        try:   
            connect = self.GenerateConect()
            cursor = connect.cursor()
            cursor.execute("INSERT INTO tbl_wish (fullname, wish) VALUES('" + data['fullname'] + "','" + data['wish'] + "')")
            connect.commit()
            return 'success'
        except Exception as ex:
            return str(ex)
        
    def Delete_Data(self, Id_Data: int):
        try:
            pass
        except Exception as ex:
            return ex
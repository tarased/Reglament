import sqlite3 as sql
import datetime


db = sql.connect('google.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS google (
    name TEXT,
    file_id TEXT,
    procedure TEXT,
    data TEXT
)""")
db.commit()


def add_note(table='google', name='Test', file_id='1xiY2tFa81K_2', procedure='Download_to'):
    data = datetime.datetime.now()
    if sql.fetchone() is None:
        sql.execute(f"INSERT into " + table + " VALUES(?, ?, ?, ?)", (name, str(file_id), procedure, data))
        db.commit()
        print('Запись успешна.')
    else:
        print('Такая запись уже имеется.')


def print_values(table='google'):
    for val in sql.execute("SELECT * FROM " + table):
        print('Name: ' + val[0] + ', File_id: ' + val[1][8:-2] + ', Procedure: ' + val[2] + ', Data: ' + val[3])


if __name__ == '__main__':
    #add_note()
    for value in sql.execute("SELECT * FROM google"):
        print(value[0])
import sqlite3 as sql


db = sql.connect('users.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    ID INT,
    email TEXT,
    login TEXT,
    password TEXT
)""")
db.commit()


def add_user(login, password, ID, email):
    sql.execute(f"SELECT login FROM users WHERE login = '{login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT into users VALUES(?, ?, ?, ?)", (ID, email, str(login), str(password)))
        db.commit()
        print('Запись успешна.')
    else:
        print('Такой пользователь уже имеется. Выберите другое имя')


def check(login, password):
    for val in sql.execute("SELECT * FROM users"):
        if val[2] == str(login):
            if val[3] == str(password):
                print('Авторизация успешна для пользователя' + str(login))
                return True
            else:
                return False
        else:
            return False


def update_password(ID, new_password):
    sql.execute(f"SELECT login FROM users WHERE ID = '{ID}'")
    if sql.fetchone() is None:
        print('Такого логина не найдено.')
    else:
        sql.execute(f"UPDATE users SET password = '{new_password}' WHERE ID = '{ID}'")


def print_values(table='users'):
    for val in sql.execute("SELECT * FROM " + table):
        print('ID: ' + str(val[0]) + ', Email: ' + val[1] + ', Login: ' + val[2] + ', Password: ' + val[3])


if __name__ == '__main__':
    add_user(login='tarased', password='12344', ID='1', email="tarased@yandex.ru")
    print_values()
    update_password(ID=1, new_password='12333333312')
    print_values()
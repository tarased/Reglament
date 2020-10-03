import sqlite3 as sql

# status = checker/admin/sender (sender - пользователь, создающий адм.рег., admin - администратор, checker - проверяю
# щая организация. login/password/ID/email - логин/пароль/ID юзера/почтовый адрес

db = sql.connect('users.db')  # соединение с базой данных
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (  
    ID INT,
    email TEXT,
    login TEXT,
    password TEXT,
    status TEXT
)""") # создание базы данных с названием users.db в случае, если она не создана
db.commit()   # сохранить изменения базы данных


def add_user(login, password, ID, email, status): # добавление пользователя с переданной информацией
    sql.execute(f"SELECT login FROM users WHERE login = '{login}'") # проверка на то, есть ли такой пользователь с таким login
    if sql.fetchone() is None:   # проверка на то, есть ли он
        sql.execute(f"INSERT into users VALUES(?, ?, ?, ?)", (ID, email, str(login), str(password), str(status))) # внесение в БД
        db.commit()  # сохранение результата
        print('Запись успешна.')
    else:
        print('Такой пользователь уже имеется. Выберите другое имя')


def check(login, password):  # проверка на присутствие пользователя в БД.
    for val in sql.execute("SELECT * FROM users"):
        if val[2] == str(login):
            if val[3] == str(password):
                print('Авторизация успешна для пользователя' + str(login))
                return True
            else:
                return False
        else:
            return False


def update_password(ID, new_password):  # смена пароля
    sql.execute(f"SELECT login FROM users WHERE ID = '{ID}'") # выбор ячейки "login" с таблицы users с определенным ID
    if sql.fetchone() is None:  # проверка на отстуствие пользователя с таким ID
        print('Такого логина не найдено.')
    else:
        sql.execute(f"UPDATE users SET password = '{new_password}' WHERE ID = '{ID}'")  # смена пароля у пользователя с опр. ID


def print_values(table='users'):  # вывод базы данных
    for val in sql.execute("SELECT * FROM " + table):
        print('ID: ' + str(val[0]) + ', Email: ' + val[1] + ', Login: ' + val[2] + ', Password: ' + val[3])


if __name__ == '__main__':
    add_user(login='tarased', password='12344', ID='1', email="tarased@yandex.ru")
    print_values()
    update_password(ID=1, new_password='12333333312')
    print_values()
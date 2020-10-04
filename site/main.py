from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
from flask_mail import Mail, Message


app = Flask(__name__)


def delete_all_statement():
    """Удаление заявления из реестра и проверки"""
    return 'Hello World !'


@app.route('/statements/', methods=['post', 'get'])
def all_statements():
    """Просмотр реестра утвержденных заявлений"""
    if request.method == 'POST':
        # Поиск по заявлениям (НЕ РЕАЛИЗОВАНО)
        search = request.form.get('search')
    return render_template('all_statements.html')


class Administration():
    def user(self):
        """Главная страница администрации"""
        return render_template('admin_main.html')
    def verification_of_statements(self):
        """Проверка заявлений администрацией"""
        pass
    def attachment_comments(self):
        """Прикрепление комментария к заявлению"""
        methods=['post', 'get']
        if request.method == 'POST':
            comment = request.form.get('comment')
            #прикрепление комментария и его последующая отправка
        return render_template('attachment_comments.html')

class Simple_User():
    def drafting_statements(self):
        """Отправка заявления на проверку"""
        return 
    def user(self):
        """Главная страница обычного пользователя"""
        #НЕ РАБОТАЕТ ПЕРЕХОД ПО КНОПКАМ
        return render_template('simple_user.html') #username=username, 
        #link=link, status=status)
    def check_statements(self):
        """Просмотр своих заявлений и их состояния"""
        pass


admin = Administration()
simple = Simple_User()


@app.route('/', methods=['post', 'get'])
def welcome_and_auth():
    """Начальная страница сайта и авторизация"""
    message = ''
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        # Сверка логина и пароля с базой данных
        if username == 'root' and password == 'pass':
            # Проверка статуса пользователя
            if True: #status == sender
                return simple.user()
            else:
                return admin.user()
        else: # При неправильном вводе данных
            message = "Неправильный логин или пароль"
    else:
        return render_template('login.html', message=message)



def dowload_pdf():
    """Скачивание PDF-файла с облака"""
    pass

def convert_in_pdf():
    """Конвертирование файла в PDF-формат"""
    pass

def save_statement():
    """Создание копии заявления на облаке"""
    pass

def delete_early_statements():
    """Удаление всех заявлений, кроме согласованого (последнего)"""
    pass

def delete_all_statement():
    """Удаление заявления из реестра и проверки"""
    pass


if __name__ == "__main__":
    app.run(debug=True)
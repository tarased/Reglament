from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, current_app
from flask_mail import Mail, Message
app = Flask(__name__)
app_context = app.app_context()
app_context.push()


username = ''

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


def administration():
    """Главная страница администрации"""
    return render_template('admin_main.html')
def verification_of_statements():
    """Проверка заявлений администрацией"""
    pass
@app.route('/comment/', methods=['post', 'get'])
def attachment_comments():
    """Прикрепление комментария к заявлению"""
    if request.method == 'POST':
        comment = request.form.get('comment')#хранит в себе комментарий
        #прикрепление комментария и его последующая отправка (смена статуса проверки)
    return render_template('attachment_comments.html')

value = 0

@app.route('/drafting_statements/', methods=['post', 'get'])
def drafting_statements():
    """Отправка заявления на проверку"""
    if request.method == 'POST':
        drafting = request.form.get('drafting') #хранит в себе регламент
        #прикрепление регламента и его последующая заливка на облако
    return render_template('drafting_statements.html')
@app.route('/checkmyreglaments/')
def check_statements():
    """Просмотр своих заявлений и их состояния"""
    return 'hello'
@app.route('/user/', methods=['post', 'get'])
def user():
    """Главная страница обычного пользователя"""
    if request.method == 'POST':
        if request.form.get('submit_button')  == 'Мои+регламенты':
            return redirect(url_for('checkmyreglaments'))
        elif request.form.get('submit_button') == 'Добавить+регламент':
            return redirect(url_for('drafting_statements'))
        elif request.form.get('submit_button') == 'Реестр+регламентов':
            return redirect(url_for('all_statements'))
    else:
        return render_template('simple_user.html', username=username)
    #link=link, status=status)


@app.route('/', methods=['post', 'get'])
def welcome_and_auth():
    """Начальная страница сайта и авторизация"""
    message = ''
    if request.method == 'POST':
        global username
        username = request.form.get('username') 
        password = request.form.get('password')
        # Сверка логина и пароля с базой данных
        if username == '' and password == '':
            # Проверка статуса пользователя
            if True: #status == sender
                return redirect(url_for('user'))
            else:
                return redirect(url_for('administration'))
        else: # При неправильном вводе данных
            message = "Неправильный логин или пароль"
    elif value == 1:
        user()
    elif value == 2:
        administration()
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

#def delete_all_statement():
    """Удаление заявления из реестра и проверки"""
    pass


if __name__ == "__main__":
    app.run(debug=True)
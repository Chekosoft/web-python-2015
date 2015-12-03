#encoding: utf-8

from flask import Flask, render_template, request, session, url_for, redirect
from forms import CreateUserForm
from modelos import Cliente
from flask_login import (LoginManager, login_user,
        login_required, current_user, logout_user)


app = Flask(__name__)
app.secret_key = 'mu903ekwiqm0cj3m129u312c8913204n321758902m'
login_manager = LoginManager()

@login_manager.user_loader
def get_user(user_id):
    try:
        return Cliente.get(id = user_id)
    except:
        return None

login_manager.login_view = 'user_login'

login_manager.init_app(app)

@app.route('/user/create', methods=['GET', 'POST'])
def user_create():
    if not current_user.is_anonymous():
        redirect(url_for('index'))

    form = CreateUserForm(request.form)

    if form.validate_on_submit():

        Cliente.create(
            username=form.username.data,
            password=form.password.data
        )

        return u'Usuario: {} creado con éxito'.format(form.username.data)

    return render_template('create_user.html', form=form)


@app.route('/user/login', methods=['GET', 'POST'])
def user_login():
    if not current_user.is_anonymous:
        redirect(url_for('index'))

    form = CreateUserForm(request.form)
    if form.validate_on_submit():
        try:
            user = Cliente.get(username = form.username.data,
                password = form.password.data)
            login_user(user)
            return redirect(url_for('index'))
        except:
            return u'Usuario o contraseña inválida'

    return render_template('login.html', form=form)

@app.route('/user/logout')
def user_logout():
    logout_user()
    return redirect(url_for('user_login'))

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return u'Hola {}'.format(nombre)

@app.route('/')
@login_required
def index():
    if 'visitas_index' in session:
        session['visitas_index'] += 1
    else:
        session['visitas_index'] = 1

    return render_template('hola.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)

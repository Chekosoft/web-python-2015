#encoding: utf-8

from flask import Flask, render_template, request
from forms import CreateUserForm
from modelos import Cliente


app = Flask(__name__)
app.secret_key = 'mu903ekwiqm0cj3m129u312c8913204n321758902m'


@app.route('/user/create', methods=['GET', 'POST'])
def user_create():
    form = CreateUserForm(request.form)

    if form.validate_on_submit():

        Cliente.create(
            username=form.username.data,
            password=form.password.data
        )

        return u'Usuario: {} creado con éxito'.format(form.username.data)

    return render_template('create_user.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)

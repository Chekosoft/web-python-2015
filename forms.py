#encoding: utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators


class CreateUserForm(Form):
    username = StringField(u'Nombre usuario', validators = [
        validators.InputRequired(message=u'Se requiere input'),
        validators.Length(message=u'Minimo 5 letras', min=5)
    ])
    password = PasswordField(u'Contraseña', validators = [
        validators.InputRequired(message=u'Input requerido'),
        validators.Length(message=u'Contraseña entre 5 y 30 letras', min=5, max=30)
    ])
    submit = SubmitField(u'Crear Usuario')

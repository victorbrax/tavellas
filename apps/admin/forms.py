# Incompleto, adaptar para essa aplicação.

from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    name = StringField('Nome Completo:', [validators.Length(min=4, max=25)])
    username = StringField('Nome de Usuário:', [
                           validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm',
                           message='Senha e Confirmação estão diferentes!')
    ])
    confirm = PasswordField('Senha')


class LoginForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [validators.DataRequired()])
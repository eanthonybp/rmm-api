from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Length, EqualTo

class RegisterForm(FlaskForm):
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.Required(),
        Length(min=4,max=24)
        ])
    password = PasswordField('New Password', [
        validators.Required(),
        EqualTo('confirm',message='Passwords must match'),
        Length(min=4, max=80)
        ])
    confirm = PasswordField('Repeat Password')
    
class LoginForm(FlaskForm):
    username = StringField('Username', [
        validators.Required(),
        validators.Length(min=4,max=25)
        ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=4, max=80)
        ])
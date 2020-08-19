from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from application.models import Admin
from flask_login import current_user 

class AdminLoginForm(FlaskForm):
    email = StringField('Email', 
    validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password', 
    validators=[
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Login')

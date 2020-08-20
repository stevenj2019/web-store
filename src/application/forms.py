from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Equalto
from application.models import Admin
from flask_login import current_user 

class AdminLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('')

class NewAdminForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Equalto('confirm', message='Passwords must match')])
    confirm = PasswordField('Password', validators=[DataRequired()])
    level = SelectField(choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('')
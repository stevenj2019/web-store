from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from application.models import Admin
from flask_login import current_user 

class AdminLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('')

class AdminForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Password', validators=[DataRequired()])
    level = SelectField(choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('')

class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('Old Password:', validators=[DataRequired()])
    new_password = PasswordField('New Password:', validators=[DataRequired(), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Confirm Password:', validators=[DataRequired()])
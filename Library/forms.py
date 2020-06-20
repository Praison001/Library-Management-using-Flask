from flask_wtf import FlaskForm  
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired, Length , Email ,EqualTo , ValidationError
from Library.model import User

class RegistrationForm(FlaskForm):
    username = StringField('username',
                            validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                            validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',
                                validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('that username is taken , please choose a different one ')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    submit = SubmitField('Login')
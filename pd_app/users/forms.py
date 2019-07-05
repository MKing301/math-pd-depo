from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from pd_app.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    last_name = StringField('Last Name', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    username = StringField('Username', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(),
                                    EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                        Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    user_request = TextAreaField(
        'Comment / Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')
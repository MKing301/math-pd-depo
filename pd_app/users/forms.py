from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
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


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.  Please choose a different one.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.  Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                        Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email.  You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(),
                                    EqualTo('password')])
    submit = SubmitField('Reset Password')


class SearchForm(FlaskForm):
    level = SelectField('Level', choices=[(1, "--- Select One ---"), (2, "K - 5"), (3, "6 - 12"), (4, "Undergraduate"), (5, "Post-Graduate")], default=1)
    topic = SelectField('Topic', choices=[(1, "--- Select One ---"), (2, "Algebra"), (3, "Calculus"), (4, "Differential Equations"), (5, "Linear Algebra")], default=1)
    keyword = StringField('Description / Keyword')
    submit = SubmitField('Search')
    clear = SubmitField('Clear')


class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    user_request = TextAreaField(
        'Comment / Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')
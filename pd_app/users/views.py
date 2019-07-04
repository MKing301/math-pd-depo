from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from pd_app.models import User
from pd_app.users.forms import RegistrationForm, LoginForm, ContactForm



users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        redirect(url_for('main.home'))
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('main.home'))
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
    
    
@users.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        user = User(request.form['first_name'],
                    request.form['last_name'], request.form['email'],
                    request.form['user_request'], datetime.utcnow())
        return redirect(url_for('users.contact'))
    else:
        return render_template('contact.html', Title="Contact", form=form)

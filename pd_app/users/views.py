from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from pd_app import db, bcrypt
from pd_app.models import User, Contact
from pd_app.users.forms import RegistrationForm, LoginForm, SearchForm, ContactForm
import pytz



users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_register = User(first_name=form.first_name.data,
                             last_name=form.last_name.data,
                             username=form.username.data,
                             email=form.email.data,
                             password=hashed_password,
                             inserted=datetime.now(pytz.timezone('US/Eastern')))
        db.session.add(user_register)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user_login = User.query.filter_by(email=form.email.data).first()
        if user_login and bcrypt.check_password_hash(user_login.password, form.password.data):
            login_user(user_login, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Signed in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('users.search'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return render_template('login.html', title='Login', form=form)
    
    
@users.route("/logout")
def logout():
    logout_user()
    flash('Signed out!', 'success')
    return redirect(url_for('main.home'))


@users.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        user_contact = Contact(first_name=form.first_name.data,
                               last_name=form.last_name.data,
                               email=form.email.data,
                               user_request=form.user_request.data,
                               created_date=datetime.now(pytz.timezone('US/Eastern')))
        db.session.add(user_contact)
        db.session.commit()
        flash('Your request have been submitted.', 'success')
        return redirect(url_for('users.contact'))
    else:
        return render_template('contact.html', title="Contact", form=form)

    
@users.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    return render_template('search.html', title="Search", form=form)

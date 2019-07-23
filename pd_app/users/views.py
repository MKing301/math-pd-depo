from datetime import datetime
from sqlalchemy import desc
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from pd_app import db, bcrypt
from pd_app.models import User, Contact
from pd_app.users.forms import RegistrationForm, LoginForm, SearchForm, ContactForm, RequestResetForm, ResetPasswordForm
from pd_app.users.utils import send_reset_email
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
                             user_role='member',
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
            if user_login.user_role == 'member':
                login_user(user_login, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('Signed in!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('users.search'))
            elif user_login.user_role == 'admin':
                login_user(user_login, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('Signed in as Admin!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('users.search'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


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


@users.route('/modify', methods=['GET', 'POST'])
@login_required
def modify():
    return render_template('modify.html', title="Add/Update/Delete")

@users.route('/member', methods=['GET', 'POST'])
@login_required
def member():
    members = db.session.query(User).order_by(desc(User.inserted)).all()
    if members:
        return render_template('member.html', title="Member", members=members)
    else:
        msg = 'No Members Found!'
        return render_template('member.html', title="Member", msg=msg)

@users.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    comments = db.session.query(Contact).order_by(desc(Contact.created_date)).all()
    if comments:
        return render_template('feedback.html', title="Feedback", comments=comments)
    else:
        msg = 'No Members Found!'
        return render_template('feedback.html', title="Feedback", msg=msg)
    return render_template('feedback.html', title="Feedback")    
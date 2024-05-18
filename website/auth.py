from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)
@auth.route('/home',)
@login_required
def home():

    return render_template("home.html", user=current_user)
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        user = User.query.filter_by(email=email).first()
        Password1 = request.form.get('Password1')
        if user:
            if User.Password1 == Password1 :
                flash('did not log in', category='error')
            else:
                flash('logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
        else:
            flash('email does not exist',category='error')

    return render_template("login.html", user=current_user)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        Password1 = request.form.get('Password1')
        Password2 = request.form.get('Password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already exists',category='error')
        elif len(email) <3:
            flash('email must be 4 characters or more', category='error')
        elif len(first_name) <2:
            flash('First name should be more than 3 characters long', category='error')
        elif Password1 != Password2:
            flash('Passwords do not match', category='error')
        elif len(Password1) <7:
            flash('password must be 8 characters or more', category='error')
        else:
            new_user = User(email=email,first_name=first_name,Password1=Password1)
            db.session.add(new_user)
            db.session.commit()
            flash('account created', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)
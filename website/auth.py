from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)
@auth.route('/home',)
def home():
    return render_template("home.html")
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        Password1 = request.form.get('Password1')
        if len(email) <3:
            flash('email must be 4 characters or more', category='error')
        elif len(first_name) <2:
            flash('First name should be more than 3 characters long', category='error')
        elif len(Password1) <7:
            flash('password must be 8 characters or more', category='error')
        else:
            flash('logged in', category='success')
    return render_template("login.html",boolean=True)
@auth.route('/logout',methods=['GET','POST'])
def logout():
    return "<p>logout</p>"
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        Password1 = request.form.get('Password1')
        Password2 = request.form.get('Password2')

        if len(email) <3:
            flash('email must be 4 characters or more', category='error')
        elif len(first_name) <2:
            flash('First name should be more than 3 characters long', category='error')
        elif Password1 != Password2:
            flash('Passwords do not match', category='error')
        elif len(Password1) <7:
            flash('password must be 8 characters or more', category='error')
        else:
            flash('account created', category='success')

    return render_template("signup.html")
from flask import Blueprint, redirect, url_for, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('app.todos'))

@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')
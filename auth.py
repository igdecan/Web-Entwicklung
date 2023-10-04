from flask import Blueprint, redirect, url_for, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from db import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('This email does not exist yet.', category='error')

        return render_template('login.html', user=current_user)

@auth.route('/logout')
def logout():
    return redirect(url_for('app.todos'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')
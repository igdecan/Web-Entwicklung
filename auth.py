from flask import Blueprint, redirect, url_for, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from db import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', 'success')
                login_user(user, remember=True)
                return redirect(url_for('todos'))
            else:
                flash('Incorrect password, try again.', 'warning')
        else:
            flash('This email does not exist yet.', 'warning')

        return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists, please log in.', 'warning')
        elif len(email) < 4:
            flash('Email must be longer than three characters.', 'warning')
        elif len(username) < 2:
            flash('Username must be longer than 1 character.', 'warning')
        elif password1 != password2:
            flash('Passwords do not match.', 'warning')
        elif len(password1) < 7:
            flash('Password needs at least seven characters.', 'warning')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created.', 'success')
            return redirect(url_for('todos'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'change_password':
            return change_password()
        elif action == 'delete_account':
            return delete_account()

    return render_template('account.html', user=current_user)

def change_password():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        new_password_hashed = generate_password_hash(new_password, method='sha256')
        current_user.password = new_password_hashed
        db.session.commit()
        flash('Password has been changed successfully.', 'success')
        return redirect(url_for('auth.account'))

    return render_template('account.html', user=current_user)

def delete_account(): 
    user = current_user
    db.session.delete(user)
    db.session.commit()

    logout_user()
    flash('Your account has been deleted.', 'success')
    return redirect(url_for('index'))
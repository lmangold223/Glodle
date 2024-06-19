from flask import Blueprint, render_template, request, flash, redirect, url_for
from . models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email is not associated with an account', category='error')
    
    return render_template('login.html', user = current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        username_check = User.query.filter_by(username=username).first()

        if user:
            flash('Email already exists.', category='error')
        elif username_check:
            flash('Username already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:

            new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('view.home'))
    return render_template('sign-up.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html', user = current_user)
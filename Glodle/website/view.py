from flask import Blueprint, render_template, request, flash

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template('index.html')

@view.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@view.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters', category='error')
        elif len(username) < 2:
            flash('Username must be at least 2 characters', category='error')
        else:
            flash('Account created!', category='success')
       
        print(email, password, username)

    
    return render_template('sign-up.html')

@view.route('/stats')
def stats():
    return render_template('stats.html')
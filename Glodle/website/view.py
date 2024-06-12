from flask import Blueprint, render_template

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template('index.html')

@view.route('/login')
def login():
    return render_template('login.html')

@view.route('/sign-up')
def signup():
    return render_template('sign-up.html')

@view.route('/stats')
def stats():
    return render_template('stats.html')
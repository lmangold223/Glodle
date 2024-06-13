from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . models import User, Guess, Album, Song
from . import db
from .database_setup import get_songs


view = Blueprint('view', __name__)

@view.route('/', methods=['GET', 'POST'])
def home():
   

    if request.method == 'POST':
        albumGuess = request.form.get('albumGuess')
        songGuess = request.form.get('songGuess')
        
        guess = Guess(song_id = songGuess, user_id = current_user.id)
        current_user.guesses_today += 1
        db.session.add(guess)
        db.session.commit()
        


    return render_template('index.html', user = current_user)


@view.route('/stats') 
@login_required
def stats():
    return render_template('stats.html', user = current_user)
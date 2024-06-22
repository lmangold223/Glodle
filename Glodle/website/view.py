from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . models import User, Guess, Album, Song, Day
import csv
from . import db
from .forms import AlbumForm, UploadForm
from .set_song import set_song_auto, pick_lyrics
import time
from werkzeug.utils import secure_filename
from .crud_operations import *

view = Blueprint('view', __name__)


# home route
@view.route('/', methods=['GET', 'POST'])
def home():

    #sets up song guessing form and populates it with choices
    album = Album.query.all()
    AlbumSelect = AlbumForm()
    AlbumSelect.album.choices = [(a.id, a.title) for a in album]

    
    #if the album table is empty, the csv file will be read and the data will be added to the database
    if len(album) == 0:
        AlbumSelect = AlbumForm()
        AlbumSelect.album.choices = [(a.id, a.title) for a in album]
        with open('website/songs.csv', encoding= "UTF-8") as csvfile:
        
            
            next(csvfile)

            songcsv = csv.reader(csvfile)

            for line in songcsv:
                
                new_album = Album(title = line[0].strip("\/,][]"), year = line[1].strip("\/,][]"), cover = line[2].strip("\/,][]"))
                db.session.add(new_album)
                db.session.commit()

                
                
                for tracklist in line[3:]:
                    for song in tracklist.split(","):
                      
                        if new_album.title == "Dirty Nachos":
                            new_song = Song(title = song.strip("\/,'][]").replace("'", "").replace("byChiefKeef & Mike WiLL Made-It", ""), album = Album.query.filter_by(title = "Dirty Nachos").first().id)
            
                            db.session.add(new_song)
                            db.session.commit()

                        else:
                            if len(song.strip("\/,][]")) > 2:
                                
                                new_song = Song(title = song.strip("\/,][]").replace("byChiefKeef", "").replace("'", ""), album = Album.query.filter_by(title = new_album.title).first().id)

                                print(new_song.title + "a: id  " + str(new_song.album))
                                db.session.add(new_song)
                                db.session.commit()
    
    
    songslist = Song.query.all()

    #handles the form submission for song guessing
    if request.method == 'POST':
        songGuess = request.form.get('song')
        songTitle = Song.query.filter_by(id = songGuess).first().title
        
    
        guess = Guess(song_title = songTitle, user_id = current_user.id, from_album = Album.query.filter_by(id = Song.query.filter_by(id = songGuess).first().album).first().title, cover_link = Album.query.filter_by(id = Song.query.filter_by(id = songGuess).first().album).first().cover, album_year = Album.query.filter_by(id = Song.query.filter_by(id = songGuess).first().album).first().year)
        current_user.guesses_today += 1

        db.session.add(guess)
        db.session.commit()\
        

    #if the song of the day has not been set, it will be set
    if Day.query.filter_by(date = time.strftime("%Y-%m-%d")).first() == None:
        set_song_auto()
    
    today = time.strftime("%Y-%m-%d")
    print(today)

    #grabs the song and lyric of the day
    song_of_the_day = Day.query.filter_by(date = today).first().song

    bar_of_the_day = Day.query.filter_by(date = today).first().bar

    song_of_the_day_album_title = Album.query.filter_by(id = Song.query.filter_by(title = song_of_the_day).first().album).first().title
    song_of_the_day_album_year = Album.query.filter_by(id = Song.query.filter_by(title = song_of_the_day).first().album).first().year

    return render_template('index.html', user = current_user, form = AlbumSelect, songs = songslist, song_of_the_day = song_of_the_day, bar_of_the_day = bar_of_the_day, album_title = song_of_the_day_album_title, album_year = song_of_the_day_album_year)


@view.route('/stats') 
@login_required
def stats():
    return render_template('stats.html', user = current_user)



# song options route for htmx request allowing for dynamic song selection
@view.route('/song_options')
def get_songs():
    
    album_id = request.args.get('album', type=int)
    songs = Song.query.filter_by(album = album_id).all()
    for song in songs:
        print(song.title)
    return render_template('song_options.html', songs = songs)


# profile route
@view.route('/profile', methods=['GET', 'POST'])
def profile():

    #handles the form submission for profile picture updating
    form = UploadForm()

    if form.validate_on_submit():

        file = form.file.data #grabs file
        file.save('website/static/files/' + secure_filename(file.filename))
        update_profile_pic(current_user.username, file.filename)
        flash('Profile Picture Updated!', 'success')



    return render_template('profile.html', user = current_user, form = form)

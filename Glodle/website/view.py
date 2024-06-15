from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . models import User, Guess, Album, Song
import csv
from . import db
from .forms import AlbumForm


view = Blueprint('view', __name__)

@view.route('/', methods=['GET', 'POST'])
def home():

    album = Album.query.all()

    AlbumSelect = AlbumForm()
    AlbumSelect.album.choices = [(a.id, a.title) for a in album]

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
                            new_song = Song(title = song.strip("\/,'][]").replace("'", "").replace("byChiefKeef & Mike WiLL Made-It", "").replace(" ", ""), album = Album.query.filter_by(title = "Dirty Nachos").first().id)
            
                            db.session.add(new_song)
                            db.session.commit()

                        else:
                            if len(song.strip("\/,][]")) > 2:
                                
                                new_song = Song(title = song.strip("\/,][]").replace("byChiefKeef", "").replace("'", ""), album = Album.query.filter_by(title = new_album.title).first().id)

                                print(new_song.title + "a: id  " + str(new_song.album))
                                db.session.add(new_song)
                                db.session.commit()
    
    
    songslist = Song.query.all()
    
    if request.method == 'POST':
        songGuess = request.form.get('song')
        songTitle = Song.query.filter_by(id = songGuess).first().title
        
    
        guess = Guess(song_title = songTitle, user_id = current_user.id, from_album = Album.query.filter_by(id = Song.query.filter_by(id = songGuess).first().album).first().title)
        current_user.guesses_today += 1

        db.session.add(guess)
        db.session.commit()


    return render_template('index.html', user = current_user, form = AlbumSelect, songs = songslist)


@view.route('/stats') 
@login_required
def stats():
    return render_template('stats.html', user = current_user)



@view.route('/get_songs')
def get_songs():
    
    album_id = request.args.get('album', type=int)
    songs = Song.query.filter_by(album = album_id).all()
    for song in songs:
        print(song.title)
    return render_template('song_options.html', songs = songs)
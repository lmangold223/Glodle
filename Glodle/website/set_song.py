import time
import lyricsgenius as lg
from .models import Album, Song, Day
from . import db
import random

#genius api key
genius = lg.Genius("BoI01P-rwaozXg13Tz2I_YqFayWUfjdyKNqHxBtytaKMkzdHxYhRJKPzQ41NEntR")

def pick_lyrics(song_title):

    #searches for the song using the genius api
    song = genius.search_song(song_title, "Chief Keef")
    print(song_title)
    if song == None:
        return "No lyrics found"
    else:
        lyrics = song.to_text()

    #splits the lyrics into bars
    bars = lyrics.split("\n")

    for bar in bars:
        
        #removes any lines we dont want to use like [Intro] or [Chorus]
        if "[" in bar:
            bars.remove(bar)
        
    #picks a random bar and the next bar
    random_bar = random.choice(bars)
    next_bar = bars[bars.index(random_bar) + 1]

    two_bars = random_bar + "\n" + next_bar

    return two_bars


#sets the song of the day automatically
def set_song_auto():
    
    #picks a random song from the database
    songs = Song.query.all()

    song = random.choice(songs)

    song_title = song.title
    album = Album.query.filter_by(id=song.album).first()

    day = Day(song=song_title, date=time.strftime("%Y-%m-%d"), bar = pick_lyrics(song_title))
    db.session.add(day)
    db.session.commit()

    
#sets the song of the day manually
def set_song_manual(song_title):

    day = Day(song=song_title, date=time.strftime("%Y-%m-%d"))
    db.session.add(day)
    db.session.commit()
    






    
        
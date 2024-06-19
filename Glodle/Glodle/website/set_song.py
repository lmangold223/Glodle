import time
import os
import lyricsgenius as lg
from .models import Album, Song, Day
from . import db
import random

genius = lg.Genius("BoI01P-rwaozXg13Tz2I_YqFayWUfjdyKNqHxBtytaKMkzdHxYhRJKPzQ41NEntR")

def set_song_auto():

    songs = Song.query.all()

    song = random.choice(songs)

    song_title = song.title
    album = Album.query.filter_by(id=song.album).first()

    day = Day(song=song_title, date=time.strftime("%Y-%m-%d"))
    db.session.add(day)
    db.session.commit()


def set_song_manual(song_title):

    day = Day(song=song_title, date=time.strftime("%Y-%m-%d"))
    db.session.add(day)
    db.session.commit()
    
def pick_lyrics(song_title):
    song = genius.search_song(song_title, "Chief Keef")
    lyrics = song.to_text()

    bars = lyrics.split("\n")

    for bar in bars:
        
        if bar.contains("["):
            bars.remove(bar)
        

    random_bar = random.choice(bars)
    next_bar = bars[bars.index(random_bar) + 1]

    two_bars = random_bar + "\n" + next_bar
    
    return two_bars





    
        
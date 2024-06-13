from .getmusic import get_songs
from . import db
from .models import Album, Song


release_dict, tracklist_dict, art_dict = get_songs()


def add_albums():
    for album in release_dict:
        new_album = Album(title = album, year = release_dict[album]['year'], cover = art_dict[album])
        db.session.add(new_album)
        db.session.commit()
        
        for song in tracklist_dict[album]:
            new_song = Song(title = song, album = new_album.id)
            db.session.add(new_song)
            db.session.commit()
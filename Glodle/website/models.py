from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    guesses_today = db.Column(db.Integer, default=0)
    guesses = db.relationship('Guess')
    streak = db.Column(db.Integer, default=0)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    cover = db.Column(db.String(150))
    year = db.Column(db.Integer)
    songs = db.relationship('Song')

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    album = db.Column(db.Integer, db.ForeignKey('album.id'))
    

class Guess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    from_album = db.Column(db.String(150))
    
    
    
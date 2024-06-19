from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, SearchField


class AlbumForm(FlaskForm):
    album = SelectField('Album', choices = [], validate_choice=False)
    song = SelectField('Song', choices =[], validate_choice=False)
    search = SearchField('Search')
    submit = SubmitField('Submit')


    
    
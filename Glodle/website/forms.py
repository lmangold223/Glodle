from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField


class AlbumForm(FlaskForm):
    album = SelectField('Album', choices = [], validate_choice=False)
    song = SelectField('Song', choices =[], validate_choice=False)
    submit = SubmitField('Submit')

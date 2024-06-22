from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, SearchField, FileField



#wtforms form classes for the website

class AlbumForm(FlaskForm):
    album = SelectField('Album', choices = [], validate_choice=False)
    song = SelectField('Song', choices =[], validate_choice=False)
    search = SearchField('Search')
    submit = SubmitField('Submit')


class UploadForm(FlaskForm):
    file = FileField('Upload File')
    submit = SubmitField('Submit')

class ChangePasswordForm(FlaskForm):
    password = StringField('Password')
    new_password = StringField('New Password')
    submit = SubmitField('Submit')


    
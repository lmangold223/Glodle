from .models import User
from . import db



# CRUD operations for User creation, retrieval, update, and deletion

def create_user(email, username, password):
    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user(username):
    user = User.query.filter_by(username=username).first()
    return user

def update_profile_pic(username, pic):
    user = User.query.filter_by(username=username).first()
    user.profile_pic = pic
    db.session.commit()
    return user

def delete_user(username):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return user

def update_password(username, password):
    user = User.query.filter_by(username=username).first()
    user.password = password
    db.session.commit()
    return user
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):
    '''
    Pitch class to define the pitch objects
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    vote_count = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship("Review", backref = "pitch", lazy = "dynamic")
    pitch_statement = db.Column(db.String())

    def like(self):
        self.likes = self.likes + 1
        self.vote_count = self.likes - self.dislikes
        db.session.add(self)
        db.session.commit()

    def dislike(self):
        self.dislikes = self.dislikes + 1
        self.vote_count = self.likes - self.dislikes
        db.session.add(self)
        db.session.commit()

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
class Review(db.Model):
    
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    pitch_title = db.Column(db.String)
    pitch_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default= datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,pitch_id):

        reviews =  Review.query.filter_by(pitch_id = id).all()
        return reviews

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        return self.pass_secure
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    def __repr__(self):
        return f'User{self.name}'
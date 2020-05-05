from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Pitch:
    '''
    Pitch class to define the pitch objects
    '''
    def __init__(self,pitch_id,pitch_type,title,pitch,author,upvotes,comments):
        self.pitch_id = pitch_id
        self.pitch_type = pitch_type
        self.title = title
        self.pitch = pitch
        self.author = author
        self.upvotes = author
        self.comments = comments

class Review:
    all_reviews = []
    def __init__(self,pitch_id,title,review):
        self.pitch_id = pitch_id
        self.title = title
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,pitch_id):
        comments = []

        for review in cls.all_reviews:
            if review.pitch_id == pitch_id:
                comments.append(review)
        
        return comments

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

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
from flask import render_template,request,redirect,url_for,abort  #takes the name of a template file as the first argument and searches and loads the file
from .import main
from ..models import Review, User
from .forms import PitchReviewForm,UpdateProfile
from .. import db
from ..models import Pitch
from flask_login import login_required


# all views below
@main.route('/')
def index():
    '''
    This is the view root function that returns the index page and its data
    '''
    
    title = 'Pitch Perfect, the best pitching website.'
    return render_template('index.html', title = title)

@main.route('/categories')
def categories():
    '''
    View categories function that returns the categories and various pitches in the category
    '''
    categories = categories()

    return render_template('categories.html')

@main.route('/user/<uname>')
def profile(uname):
    '''
    View function to display the profile of a logged in user
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/comments')
def comments():
    '''
    This is the view function to display the comments and reviews.
    '''
    
    reviews = Review.get_reviews(id)

    return render_template('pitch.html',reviews = reviews)

@main.route('/pitch/review/new', methods = ['GET','POST'])
@login_required
def new_review():
    '''
    View function for the reviews and comments
    '''
    form = PitchReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = review(title,review)
        new_review.save_review()
    


    return render_template('/review.html',pitch_review_form = form)


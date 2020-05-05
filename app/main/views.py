from flask import render_template #takes the name of a template file as the first argument and searches and loads the file
from .import main
from ..models import Review
from .forms import PitchReviewForm
from ..models import Pitch


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

@main.route('/profile')
def profile():
    '''
    View function to display the profile of a logged in user
    '''

    profile = profile()

    return render_template('profile.html')

@main.route('/comments')
def comments():
    '''
    This is the view function to display the comments and reviews.
    '''
    
    reviews = Review.get_reviews(id)

    return render_template('pitch.html',reviews = reviews)

@main.route('/pitch/review/new', methods = ['GET','POST'])
def comment_review():
    '''
    View function for the reviews and comments
    '''
    form = PitchReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        comment_review = review(title,review)
        comment_review.save_review()
    


    return render_template('/review.html',pitch_review_form = form)


from flask import render_template #takes the name of a template file as the first argument and searches and loads the file
from app import app

# all views below
@app.route('/')
def index():
    '''
    This is the view root function that returns the index page and its data
    '''
    return render_template('index.html')
    
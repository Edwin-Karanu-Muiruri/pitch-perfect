from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchReviewForm(FlaskForm):
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself',validators = [Required()])
    submit = SubmitField('Submit')
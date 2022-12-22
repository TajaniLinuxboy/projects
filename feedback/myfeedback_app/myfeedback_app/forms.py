from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email, Length


class FeedBackForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()], Length(7, 40))
    email = EmailField('email', validators=[DataRequired(), Email(), Length(15, 50)])
    comment = TextAreaField('comment', validators=[DataRequired()])

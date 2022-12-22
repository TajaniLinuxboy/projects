from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo, URL
from app.database_models import Users



class SignUp(FlaskForm):
    username = StringField("Username", validators=[
    DataRequired(), Length(5, 30)
    ])
    email = StringField("Email", validators=[
    DataRequired(), Email()
    ])
    password = PasswordField("PasswordField", validators=[
    DataRequired()
    ])
    submit = SubmitField("Sign up")

    def validate_email(self, user_email):
        user = Users.query.filter_by(email=user_email.data).first()
        if user:
            return ValidationError("Email already exist")

    def validate_user(self, user):
        user = Users.query.filter_by(username=user.data).first()
        if user:
            return ValidationError("Username already exists")



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
    DataRequired(), Email(), Length(10, 70)
    ])
    password = PasswordField("Password", validators=[
    DataRequired(), Length(5, 30)
    ])
    remember_user = BooleanField("Remember me")
    submit = SubmitField("Login")


class RequestResetPasswordForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Request Reset Password')

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", "Password is not the same")])
    submit = SubmitField("Reset Password")


class StoreLinksForm(FlaskForm):
    link = StringField("Link", validators=[DataRequired(), URL()])
    title = StringField("Title", validators=[DataRequired()])

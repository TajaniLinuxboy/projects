from flask import render_template, request, redirect, url_for, flash, jsonify, make_response, session
from app import app, bcrypt, db
from app.forms import SignUp, LoginForm, RequestResetPasswordForm, ResetPasswordForm, StoreLinksForm
from app.database_models import Users, StoreLinks
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from sqlalchemy import exc
from datetime import timedelta
import logging
from itsdangerous.serializer import Serializer
from app.custom_classes import CustomSerializer


logging.basicConfig(filename="app.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

@app.route("/", methods=["GET"])
def index():
    if current_user.is_authenticated:
        app.logger.info("User already authenticated")
        return redirect(url_for("account"))
        app.logger.info("Client redirected to signup")
    return redirect(url_for("signup"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    form = SignUp()
    if form.validate_on_submit():
        hash_paswd = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = Users(username=form.username.data, email=form.email.data, password=hash_paswd)

        try:
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            return redirect(url_for("login"))
        except exc.IntegrityError:
            db.session.rollback()

    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.cookies.get("remember_token"):
        return redirect(url_for('account'))

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_user.data, duration=timedelta(minutes=30))
            return redirect(url_for("account"))
        else:
            flash("Login Unsucessful. Please Try Again", "failed")

    return render_template("login.html", form=form)

s = Serializer(app.config["SECRET_KEY"])

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html")



@app.route("/insertUrl", methods=["POST", "GET"])
@login_required
def insertUrl():
    resp = request.get_json()["data"]
    link_obj = StoreLinks(link=resp['url'], link_title=resp['title'])

    try:
        db.session.add(link_obj)
        db.session.flush()
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()

    return None



@app.route("/linkinfo/<user_id>", methods=["GET"])
@login_required
def linkinfo(user_id):
    user = s.loads(user_id)['user_id']
    query = StoreLinks.query.filter_by(user_id=user_id)

    user_data = {
        "title": query.link_title.first(),
        "link": StoreLinks.query.order_by(query.link).all()
    }

    return make_response(jsonify(user_data))




@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
    "Password Reset Request",
    sender='no-replay@gmail.com',
    recipients=[user.email]
    )


    msg.body = f"To Reset Your Password Click This Link: {url_for('reset_token', token=token, _external=True)}"

@app.route("/requestPasswordChange", methods=["GET", "POST"])
def requestPasswordChange():
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    form = RequestResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("Check Email for more information")
        return redirect(url_for('login'))
    return render_template("requestPassword.html", title="Reset Password", form=form)

@app.route("/resetPassword/<token>", methods=["GET", "POST"])
def resetPassword(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)

    if user is None:
        flash('Invalid/Expired Token')
        return redirect(url_for('resetPassword'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash("Successful")
        return redirect(url_for('login'))

    return render_template("resetPassword.html", title="Request Password Change", form=form)

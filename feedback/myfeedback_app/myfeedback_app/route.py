from myfeedback_app import app
from flask import url_for, redirect, render_template
from myfeedback_app.forms import FeedBackForm

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for('feedbackform'))


@app.route("/feedbackform", methods=["GET", "POST"])
def feedbackform():
    form = FeedBackForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', form=form)


@app.route("/success")
def success():
    return '<h1> Form Completed </h1>'

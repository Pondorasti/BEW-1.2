from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .. import app, db, bcrypt
from ..models import User
from .forms import SignUpForm, LoginForm

auth = Blueprint("auth", __name__)

# Routes


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash("New user created!")

        return redirect(url_for("auth.login"))

    return render_template("signup.html", form=form, action="/signup")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
        next_page = request.args.get("next")
        return redirect(next_page if next_page else url_for("main.homepage"))

    return render_template("login.html", form=form, action="/login")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.homepage"))

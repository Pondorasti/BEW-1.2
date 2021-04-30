from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
import flask_login

from .. import app, db
from ..models import Sprint, Task
from .forms import SprintForm

main = Blueprint("main", __name__)

# Routes


@main.route("/")
def homepage():
    sprints = Sprint.query.all()
    return render_template("home.html", sprints=sprints)


@main.route("/create_sprint", methods=["GET", "POST"])
@login_required
def create_sprint():
    form = SprintForm()

    if form.validate_on_submit():
        sprint = Sprint(name=form.name.data, created_by_id=current_user.id)

        db.session.add(sprint)
        db.session.commit()

        flash("New Sprint created!")

        return redirect(url_for("main.homepage"))

    return render_template("create_sprint.html", form=form)


@main.route("/sprint/<sprint_id>", methods=["GET", "POST"])
@login_required
def sprint_detail(sprint_id):
    sprint = Sprint.query.get(sprint_id)
    form = SprintForm(obj=sprint)

    if form.validate_on_submit():
        sprint.name = form.name.data
        db.session.commit()

        flash("Sprint succefully updated!")

    return render_template("sprint_detail.html", sprint=sprint, form=form)

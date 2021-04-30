from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import app, db
from ..models import Sprint, Task
from .forms import SprintForm, TaskForm

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

        flash("New sprint created!")

        return redirect(url_for("main.sprint_detail", sprint_id=sprint.id))

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


@main.route("/create_task", methods=["GET", "POST"])
@login_required
def create_task():
    form = TaskForm()

    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            difficulty=form.difficulty.data,
            sprint=form.sprint.data
        )

        db.session.add(task)
        db.session.commit()

        flash("New task created!")

        return redirect(url_for("main.task_detail", task_id=task.id))

    return render_template("create_task.html", form=form)


@main.route("/task/<task_id>", methods=["GET", "POST"])
@login_required
def task_detail(task_id):
    task = Task.query.get(task_id)
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.difficulty = form.difficulty.data
        task.sprint = form.sprint.data

        db.session.commit()

        flash("Task succefully updated!")

    return render_template("task_detail.html", task=task, form=form)

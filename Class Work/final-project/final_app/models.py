from flask_login import UserMixin
from . import db
from .utils import FormEnum


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


class Sprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    tasks = db.relationship("Task", back_populates="sprint")

    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_by = db.relationship("User")

    def __repr__(self):
        return self.name


class TaskDifficulty(FormEnum):
    EASY = "Easy Peazy"
    MEDIUM = "Cool Taks"
    HARD = "Boooring"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(400))
    difficulty = db.Column(
        db.Enum(TaskDifficulty), default=TaskDifficulty.MEDIUM
    )

    sprint_id = db.Column(
        db.Integer, db.ForeignKey("sprint.id"), nullable=False
    )
    sprint = db.relationship("Sprint", back_populates="tasks")

    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_by = db.relationship("User")

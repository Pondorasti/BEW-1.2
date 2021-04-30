from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length
from ..models import Sprint, TaskDifficulty


class SprintForm(FlaskForm):
    name = StringField(
        label="Name", validators=[DataRequired(), Length(min=3, max=20)]
    )
    submit = SubmitField(label="Submit")


class TaskForm(FlaskForm):
    title = StringField(
        label="Title", validators=[DataRequired(), Length(min=3, max=20)]
    )
    description = TextAreaField(
        label="Description", validators=[Length(max=400)]
    )
    difficulty = SelectField(
        "Difficulty", validators=[DataRequired()], choices=TaskDifficulty.choices()
    )
    sprint = QuerySelectField(
        "Sprint", validators=[DataRequired()], query_factory=lambda: Sprint.query
    )
    submit = SubmitField("Submit")

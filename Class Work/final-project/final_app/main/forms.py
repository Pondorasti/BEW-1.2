from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from ..models import Sprint


class SprintForm(FlaskForm):
    name = StringField(
        label="Name", validators=[DataRequired(), Length(min=3, max=20)]
    )
    submit = SubmitField(label="Create Sprint")

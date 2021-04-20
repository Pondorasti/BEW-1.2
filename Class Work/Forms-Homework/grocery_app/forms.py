from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.core import FloatField
from wtforms.validators import DataRequired, Length, NumberRange, URL
from grocery_app.models import GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField("Title", validators=[
                        DataRequired(), Length(min=3, max=16)])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField("Name", validators=[
                       DataRequired(), Length(min=3, max=16)])
    price = FloatField("Price $", validators=[
                       DataRequired(), NumberRange(min=0)])
    category = SelectField("Category", validators=[
                           DataRequired()], choices=ItemCategory.choices())
    photo_url = StringField("Photo URL", validators=[URL()])
    store = QuerySelectField("Store", validators=[
                             DataRequired()], query_factory=lambda: GroceryStore.query)
    submit = SubmitField("Submit")

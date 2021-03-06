from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length
from books_app.models import Audience, Book, Author, Genre


class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', validators=[
                        DataRequired(), Length(min=3, max=80)])
    publish_date = DateField('Date Published')
    author = QuerySelectField(
        'Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField(
        'Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')


class AuthorForm(FlaskForm):
    """Form to create an author."""

    # TODO: Fill out the fields in this class for:
    # - the author's biography (hint: use a TextAreaField)
    # - a submit button
    name = StringField("Author Name", validators=[
                       DataRequired(), Length(min=3, max=80)])
    biography = TextAreaField("Author Biography", validators=[
                              DataRequired(), Length(min=10, max=200)])
    submit = SubmitField("Submit")
    pass


class GenreForm(FlaskForm):
    """Form to create a genre."""

    # TODO: Fill out the fields in this class for:
    # - the genre's name (e.g. fiction, non-fiction, etc)
    # - a submit button
    pass

import os
from unittest import TestCase

from datetime import date

from books_app import app, db, bcrypt
from books_app.models import Book, Author, User, Audience

"""
Run these tests with the command:
python -m unittest books_app.main.tests
"""

#################################################
# Setup
#################################################

user_data = {
    "username": "me1",
    "password": "password"
}


def create_books():
    a1 = Author(name='Harper Lee')
    b1 = Book(
        title='To Kill a Mockingbird',
        publish_date=date(1960, 7, 11),
        author=a1
    )
    db.session.add(b1)

    a2 = Author(name='Sylvia Plath')
    b2 = Book(title='The Bell Jar', author=a2)
    db.session.add(b2)
    db.session.commit()


def create_user():
    password_hash = bcrypt.generate_password_hash(
        user_data["password"]
    ).decode('utf-8')
    user = User(username=user_data["username"], password=password_hash)
    db.session.add(user)
    db.session.commit()

#################################################
# Tests
#################################################


class AuthTests(TestCase):
    """Tests for authentication (login & signup)."""

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_signup(self):
        self.app.post("/signup", data=user_data)

        created_user = User.query.filter_by(
            username=user_data["username"]
        ).one()
        self.assertIsNotNone(created_user)

    def test_signup_existing_user(self):
        self.app.post("/signup", data=user_data)
        res = self.app.post("/signup", data=user_data)
        res_text = res.get_data(as_text=True)

        self.assertIn(
            "That username is taken. Please choose a different one.", res_text
        )

    def test_login_correct_password(self):
        create_user()

        res = self.app.post("/login", data=user_data, follow_redirects=True)
        res_text = res.get_data(as_text=True)

        self.assertNotIn("login", res_text)

    def test_login_nonexistent_user(self):
        res = self.app.post("/login", data=user_data)
        res_text = res.get_data(as_text=True)

        self.assertIn(
            "No user with that username. Please try again.", res_text
        )

    def test_login_incorrect_password(self):
        create_user()

        incorrect_user_data = {
            "username": user_data["username"],
            "password": user_data["username"]
        }

        res = self.app.post("/login", data=incorrect_user_data)
        res_text = res.get_data(as_text=True)

        self.assertIn(
            "Password doesn&#39;t match. Please try again.",
            res_text
        )

    def test_logout(self):
        create_user()
        self.app.post("/login", data=user_data)

        res = self.app.post("/logout", follow_redirects=True)
        res_text = res.get_data(as_text=True)

        self.assertNotIn("login", res_text)

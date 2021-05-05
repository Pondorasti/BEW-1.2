import unittest

from .. import app, db, bcrypt
from ..models import User

user_data = {
    "username": "alex",
    "password": "password"
}


def create_user():
    password_hash = bcrypt.generate_password_hash(
        user_data["password"]
    ).decode("utf-8")
    user = User(username=user_data["username"], password=password_hash)

    db.session.add(user)
    db.session.commit()


class AuthTests(unittest.TestCase):
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
        self.assertIsNotNone(create_user)
        self.assertEqual(created_user.username, user_data["username"])

    def test_login_correct_password(self):
        create_user()

        res = self.app.post("/login", data=user_data, follow_redirects=True)
        res_text = res.get_data(as_text=True)

        self.assertNotIn("login", res_text)

    def test_login_nonexistent_user(self):
        res = self.app.post("/login", data=user_data)
        res_text = res.get_data(as_text=True)

        self.assertIn(
            "This username does not exist in the database.", res_text
        )

    def test_logout(self):
        create_user()
        self.app.post("/login", data=user_data)

        res = self.app.post("/logout", follow_redirects=True)
        res_text = res.get_data(as_text=True)

        self.assertNotIn("login", res_text)

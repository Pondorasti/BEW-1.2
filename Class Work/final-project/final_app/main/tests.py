import unittest

from .. import app, db, bcrypt
from ..models import User, Sprint


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


def login(client, data):
    return client.post("/login", data=data, follow_redirects=True)


def logout(client):
    return client.post("/logout", follow_redirects=True)


class MainTests(unittest.TestCase):
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_homepage_logged_out(self):
        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)

        res_text = res.get_data(as_text=True)
        self.assertIn("Sign Up", res_text)
        self.assertIn("Log In", res_text)

        self.assertNotIn("Create Task", res_text)
        self.assertNotIn("Create Sprint", res_text)
        self.assertNotIn("Log Out", res_text)

    def test_homepage_logged_in(self):
        create_user()
        login(self.app, user_data)

        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)

        res_text = res.get_data(as_text=True)
        self.assertNotIn("Sign Up", res_text)
        self.assertNotIn("Log In", res_text)

        self.assertIn("Create Task", res_text)
        self.assertIn("Create Sprint", res_text)
        self.assertIn("Log Out", res_text)

    def test_create_sprint(self):
        create_user()
        login(self.app, user_data)

        sprint_data = {"name": "sprint"}

        self.app.post("/create_sprint", data=sprint_data)

        created_sprint = Sprint.query.filter_by(name="sprint").one()
        self.assertIsNotNone(created_sprint)
        self.assertEqual(created_sprint.name, "sprint")

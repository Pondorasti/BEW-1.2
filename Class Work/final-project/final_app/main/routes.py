from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from final_app import app, db

main = Blueprint("main", __name__)

# Routes


@main.route("/")
def homepage():
    return "Hello, Alex"

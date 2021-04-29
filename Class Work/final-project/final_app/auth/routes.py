from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from final_app import app, db

auth = Blueprint("auth", __name__)

# Routes


@auth.route("/signup")
def homepage():
    return "Soon TM"

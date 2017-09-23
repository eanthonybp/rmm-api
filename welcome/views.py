from flask_init import app
from flask import render_template, redirect, url_for, session, request


@app.route('/welcome')
def welcome():
    return "This is the Welcome Page!"
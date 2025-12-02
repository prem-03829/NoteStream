from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return "<h1>Project NoteStream is Live!</h1>"
from flask import render_template, Blueprint, redirect, url_for, request
from .models import db, Note

main = Blueprint('main', __name__)

@main.route("/")
def index():
    notes = Note.query.all()
    return render_template('index.html', notes = notes)

@main.route("/create", methods = ["POST", "GET"])
def create():
    if request.method == "POST":
        new_note = Note()
        new_note.title = request.form.get("title")
        new_note.content = request.form["content"]
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for("main.index"))

    else:
        return render_template("create_note.html")
    
@main.route("/delete/<int:id>", methods = ["POST"])
def delete(id):
    note = Note.query.filter_by(id = id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/edit/<int:id>", methods = ["POST", "GET"])
def edit(id):
    note = Note.query.filter_by(id = id).first_or_404()
    if request.method == "POST":
        note.title = request.form.get("title")
        note.content = request.form.get("content")    
        db.session.commit()
        return redirect(url_for("main.index"))
    else:
        return render_template("edit_note.html", note = note)
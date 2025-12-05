from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.now(timezone.utc))

    tags = db.relationship("Tag", secondary="note_tags", backref = "notes", lazy = True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True)

note_tags = db.Table(
    'note_tags', 
    db.Model.metadata,
    db.Column('note_id', db.Integer, db.ForeignKey('note.id'), primary_key = True), 
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key = True)
)
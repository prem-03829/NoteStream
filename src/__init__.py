from flask import Flask
from .routes import main
from .models import db, Note, Tag, note_tags

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'need-something-here'
    app.register_blueprint(main)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notestream.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
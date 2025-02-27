# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    thumbnail = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(1023), nullable=False)
    tags = db.Column(db.String(1023), nullable=True)  # Simple comma-separated tags

    def __repr__(self):
        return f"<Link {self.url}>"

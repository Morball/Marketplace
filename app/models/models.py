from flask_sqlalchemy import SQLAlchemy
from app import app
db=SQLAlchemy(app)
from datetime import datetime


class Listing(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80),unique=True,nullable=False)
    price=db.Column(db.Float,nullable=False)
    description=db.Column(db.String(1200),nullable=False)
    category=db.Column(db.String(80), nullable=False)
    location=db.Column(db.String(80),nullable=False)
    shipsTo=db.Column(db.String(80),nullable=False)
    approved=db.Column(db.Boolean,nullable=False,default=False)
    listedAt=db.Column(db.DateTime,nullable=True,default=datetime.now())
    vendor=db.Column(db.String(80),nullable=True)
    def __repr__(self):
        return f"product('{self.name}','{self.price}','{self.description}')"

class PrivateMessage(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sender=db.Column(db.String(80),nullable=False)
    receiver=db.Column(db.String(80),nullable=False)
    message=db.Column(db.String(1200),nullable=False)
    sentAt=db.Column(db.DateTime, nullable=False, default=datetime.now())
    def __repr__(self):
        return f"message('{self.sender}','{self.receiver}','{self.message}')"



class Review(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.String(80),nullable=False)
    vendor=db.Column(db.String(80),nullable=True)
    product_id=db.Column(db.String(80),nullable=False)
    review=db.Column(db.String(1200),nullable=False)
    timestamp=db.Column(db.DateTime, nullable=False, default=datetime.now())
    experience=db.Column(db.String(80),nullable=True)
    def __repr__(self):
        return f"review('{self.user}','{self.product}','{self.review}')"


class Ticket(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80), nullable=False)
    content=db.Column(db.String(1200), nullable=False)
    creator=db.Column(db.String(80), nullable=False)
    category=db.Column(db.String(80), nullable=False)
    is_active=db.Column(db.Boolean, nullable=False)
    updated_at=db.Column(db.DateTime, nullable=False)
    updated_by=db.Column(db.String(80), nullable=False)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)
    role=db.Column(db.String(80),nullable=False)
    last_login=db.Column(db.DateTime)
    trustScore=db.Column(db.Float,nullable=True,default=0)
    def __repr__(self):
        return f"user('{self.username}')"
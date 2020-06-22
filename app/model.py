from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    email =db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"user '{self.username}' ,'{self.email}'"

class Books(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    ISBN= db.Column(db.Integer(50), unique=True, nullable=False)
    author= db.Column(db.String(70), nullable=False)
    title= db.Column(db.String(100), nullable=False)
    pub_year= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"bookDetail '{self.ISBN}', '{self.author}', '{self.title}', '{self.pub_year}'"



from datetime import datetime
from application import db, login_manager
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





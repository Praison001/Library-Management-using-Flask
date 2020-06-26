from flask import render_template, url_for, request , redirect,flash, Flask
from app import *
from app.forms import RegistrationForm , LoginForm, User
from flask_login import login_user, current_user , logout_user , login_required, LoginManager
import requests
import json
import random
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String, VARCHAR
from sqlalchemy.orm import sessionmaker
import csv
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# #Creating table for Users
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_manager_catogory = 'info' 

#Creating table for importing csv
engine = create_engine('sqlite:///Books.db' , echo=True , connect_args={'check_same_thread':False})
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Books(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    ISBN = Column(VARCHAR(100) , nullable=False)
    Title= Column(VARCHAR(100) , nullable=False)
    Author= Column(VARCHAR(100) , nullable=False)
    Pub_year= Column(VARCHAR(100) , nullable=False)

    def __repr__(self):
        return f"{self.ISBN} {self.Title}"
    
Base.metadata.create_all(engine)

@app.route("/")
def index():
    with open('books.csv','r') as fin:
        dr = csv.DictReader(fin)
        for i in dr:
            obj = Books(ISBN= i["ISBN"], Title= i["Title "], Author= i["Author"], Pub_year= i["Pub_year"])
            session.add(obj)
            session.commit()
    return render_template("search.html")

#Registration
@app.route("/register",methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(('/index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('your account has been created')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

#Login
@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print("user",user)
        if user and bcrypt.check_password_hash(user.password , form.password.data):
                return redirect(url_for('index'))
        else:
            flash("login unsuccessful")
    return render_template('login.html',title='Login',form=form)

@app.route('/search', methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        if request.form.get("author"):
                """
                return rendered result.html page with books from Google Books API written by the provided author that match
                search results
                """
                return render_template("searchResults.html", books = requests.get("https://www.googleapis.com/books/v1/volumes?q=" +
                                request.form.get("title") + "+inauthor:" + request.form.get("author") +
                                "&key=AIzaSyCFCQqFEtO1osFjZaQnoyYSs8Aylo7ZRVM").json())


if __name__ == '__main__':
    session= Session()
    app.run(debug=True)


    
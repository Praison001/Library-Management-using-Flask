from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app import routers
import csv
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_manager_catogory = 'info' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Books.db'
db1 = SQLAlchemy(app)


# con = sqlite3.connect(":memory:") # change to 'sqlite:///your_filename.db'
# cur = con.cursor()
# cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

# with open('data.csv','r') as data: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(data) # comma is default delimiter
#     to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, url_for, request , redirect,flash
from Library import app ,db ,bcrypt ,login_manager
from Library.forms import RegistrationForm , LoginForm, User
from flask_login import login_user, current_user , logout_user , login_required

@app.route('/index')
def index():
    return render_template("index.html")

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
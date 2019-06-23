from app import app, db, login_manager
from app.models.tables import User, Post
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.models.forms import LoginForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    #db.session.add(User(username="Flask", email="example@example.com"))
    #db.session.commit()
    #db.session.add(Post('Teste de conteúdo 2', 2))
    #db.session.commit()

    #users = User.query.all()
    #print(users)

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid Login.')
    else:
        print(form.errors)

    return render_template('login.html',
        form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
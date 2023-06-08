from flask import Flask
from flask import render_template, request, redirect
from flask_login import login_user, logout_user, login_required
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from pokemon_app import app
from pokemon_app import db
from pokemon_app.models.tables import User


@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    print(request.form)
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        # Userのインスタンスを作成
        user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('users/signup.html')
    

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        # Userテーブルからusernameに一致するユーザを取得
        user = User.query.filter_by(name=name).first()
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect('/')
    else:
        return render_template('users/login.html')

@app.route('/users/logout')
def logout():
    logout_user()
    return redirect('/login')
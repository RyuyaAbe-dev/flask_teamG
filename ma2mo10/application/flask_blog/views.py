from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
# リクエストがあった時の処理  ラッパーに渡す
def show_entries():
    return render_template('entries/index.html')
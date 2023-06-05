from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps


def login_required(view):
    '''セッション情報を参照し、ログインしていないとき(session[logged_in] = Falseのとき)の処理'''
    @wraps(view)
    # デコレータにする
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            # ログインページに遷移
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@app.route('/login', methods=['GET', 'POST'])
# ログイン処理
def login():
    if request.method == 'POST':
        # ユーザ名が異なるとき
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        # パスワードが異なるとき
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            # session['logged_in']にTrueをセット(ログイン状態にする)
            session['logged_in'] = True
            # ログイン成功メッセージ
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
# ログアウト処理
def logout():
    # ログアウトしたのでセッション情報を削除
    session.pop('logged_in', None)
    return redirect(url_for('show_entries'))
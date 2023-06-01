from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
# リクエストがあった時の処理  ラッパーに渡す
def show_entries():
    # セッション情報を参照し、ログインしていないとき(session[logged_in] = Trueのとき)の処理
    if not session.get('logged_in'):
        return redirect('/login')

    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
# ログイン処理
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            # session['logged_in']にTrueをセット(ログイン状態にする)
            session['logged_in'] = True
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
# ログアウト処理
def logout():
    # ログアウトしたのでセッション情報を削除
    session.pop('logged_in', None)
    return redirect('/')
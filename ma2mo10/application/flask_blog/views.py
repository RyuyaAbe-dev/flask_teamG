from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
# リクエストがあった時の処理  ラッパーに渡す
def show_entries():
    # セッション情報を参照し、ログインしていないとき(session[logged_in] = Falseのとき)の処理
    if not session.get('logged_in'):
        # ログインページに遷移
        return redirect('/login')
    # ログインしているとき(session[logged_in] = True)の処理
    # トップページに遷移
    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
# ログイン処理
def login():
    if request.method == 'POST':
        # ユーザ名が異なるとき
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
        # パスワードが異なるとき
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
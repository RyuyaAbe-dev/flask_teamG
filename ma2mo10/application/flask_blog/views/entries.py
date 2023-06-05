from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required

@app.route('/')
@login_required
# リクエストがあった時の処理  ラッパーに渡す
def show_entries():
    # ログインしているとき(session[logged_in] = True)の処理
    # エントリの一覧を取得
    entries = Entry.query.order_by(Entry.id.desc()).all()
    # トップページに遷移
    return render_template('entries/index.html', entries=entries)


@app.route('/entries/new', methods=['GET'])
@login_required
def new_entry():
    '''新規作成のページに飛ぶ'''
    # 新規作成のページに遷移
    return render_template('entries/new.html')

@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    '''新規の記事を追加する'''
    # フォームに入力した内容をカラムにセットする
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    # SQLを流す
    # 追加コマンド
    db.session.add(entry)
    # コミット
    db.session.commit()
    # メッセージの表示
    flash('新しく記事が作成されました')
    # トップページに遷移
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>', methods=['GET'])
@login_required
def show_entry(id):
    '''記事を閲覧するページに飛ぶ'''
    # テーブルから記事の中身を取得
    entry = Entry.query.get(id)
    # 個別記事の閲覧ページに遷移
    return render_template('entries/show.html', entry=entry)

@app.route('/entries/<int:id>/update', methods={'POST'})
@login_required
def update_entry(id):
    '''記事を更新する'''
    entry = Entry.query.get(id)
    # フォームに入力したタイトルとテキストを格納
    entry.title = request.form['title']
    entry.text = request.form['text']
    # SQLを流す
    # データの更新
    db.session.merge(entry)
    # コミット
    db.session.commit()
    # メッセージの表示
    flash('記事が更新されました')
    # トップページに遷移
    return  redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    '''記事を更新するページに飛ぶ'''
    # 更新する記事の中身を取得
    entry = Entry.query.get(id)
    # 編集ページに遷移
    return render_template('entries/edit.html', entry=entry)

@app.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    '''記事を削除する'''
    entry = Entry.query.get(id)
    # SQLを流す
    # データを削除
    db.session.delete(entry)
    # コミット
    db.session.commit()
    # メッセージの表示
    flash('投稿が削除されました')
    # トップページに遷移
    return redirect(url_for('show_entries'))
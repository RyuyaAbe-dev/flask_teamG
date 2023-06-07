from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/')
def show_input():
    return render_template('input.html')

@app.route('/show_result', methods=['GET'])
def show_result():
    return render_template('result.html')

@app.route('/button_control', methods=['POST'])
def button_control():
    input_date = request.form['holiday']        # 入力データ(日付)
    input_text = request.form['holiday_text']   # 入力データ(祝日の名前)
    # 入力された日付の祝日が登録されていればテーブルから抽出
    date = Holiday.query.filter(Holiday.holi_date==input_date).first()

    button_type = request.form["button"]        # 押されたボタンの種類

    if button_type == 'edit':
        if date == None:
            # 新規作成の場合
            # インスタンスを生成
            holiday = Holiday(
                    holi_date=input_date,
                    holi_text=input_text
                    )
            # レコードを追加
            db.session.add(holiday)
            # コミット
            db.session.commit()
            # 結果画面上で表示するテキストをセッションとして持っておく
            session['result_text'] = f"{request.form['holiday']}({request.form['holiday_text']})が登録されました"
            return redirect(url_for('show_result'))
        else:
            # 変更の場合
            holiday = date
            holiday.holi_text=input_text
            # 更新
            db.session.merge(holiday)
            # コミット
            db.session.commit()
            # 結果画面上で表示するテキストをセッションとして持っておく
            session['result_text'] = f"{request.form['holiday']}は「{request.form['holiday_text']}」に更新されました"
            return redirect(url_for('show_result'))
    
    elif button_type == 'delete':
        if date == None:
            # 削除の場合
            flash(f'{date}は祝日マスタに登録されていません')
            return render_template('input.html')
        holiday = date
        # 指定された日付のレコードを削除
        db.session.delete(holiday)
        # コミット
        db.session.commit()
        # 結果画面上で表示するテキストをセッションとして持っておく
        session['result_text'] = f"{request.form['holiday']}({request.form['holiday_text']})が削除されました"
        return redirect('show_result')

@app.route('/show_list')
def show_list():
    holiday_list = Holiday.query.order_by(Holiday.holi_date).all()
    # 一覧ページに遷移
    return render_template('list.html', holiday_list=holiday_list)

# @app.route('/result', methods=['POST'])
# def new_holiday():
#     holiday = Holiday(
#         holi_date = request.form['holiday'],
#         holi_text = request.form['holiday_text']
#     )

#     db.session.add(holiday)
#     # コミット
#     db.session.commit()
#     # メッセージの表示
#     session['result_text'] = f"{request.form['holiday']}({request.form['holiday_text']})が登録されました"
#     return redirect(url_for('show_result'))
    



# @app.route('/result', methods=['POST'])
# def delete_holiday():
#     holiday = Holiday.query.get(db.and_(holi_date = request.form['holiday'], holi_text = request.form['holiday_text']))
#     db.session.delete(holiday)
#     db.session.commit()
#     session['result_text'] = f"{request.form['holiday']}({request.form['holiday_text']})が削除されました"
#     return redirect('show_result')



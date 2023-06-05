from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
import datetime

@app.route('/')
def display_input():
    return render_template('input.html')

@app.route('/list')
def show_holidays():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidays=holidays)



@app.route('/operate_data', methods=['POST'])
def operate_data():
    print(request.form)
    input_date = request.form["holi_date"]
    input_text = request.form["holi_text"]
    target_date = Holiday.query.filter(Holiday.holi_date==input_date).first()
    btn_type = request.form["button"] 
    if btn_type == "delete":
        if target_date == None:
            print('aaaa')
            flash(f'{input_date}は祝日マスタに登録されていません')
            return render_template('input.html')
        holiday = target_date
        db.session.delete(holiday)
        db.session.commit()
        return render_template('result.html', holiday=holiday, btn_type = btn_type)
    elif btn_type == "new_edit":
        if target_date == None:
            # new
            holiday = Holiday(
                    holi_text=input_text,
                    holi_date=input_date
                    )
            db.session.add(holiday)
            db.session.commit()
            return render_template('result.html', holiday=holiday, btn_type = "new")
        else:
            holiday = target_date
            holiday.holi_text=input_text
            db.session.merge(holiday)
            db.session.commit()
            return render_template('result.html', holiday=holiday, btn_type = "update")
    else:
        print('error')


# @app.route('/entries/new', methods=['GET'])
# def new_entry():
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     return render_template('entries/new.html')

# @app.route('/entries/<int:id>', methods=['GET'])
# def show_entry(id):
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     entry = Entry.query.get(id)
#     return render_template('entries/show.html', entry=entry)


# @app.route('/entries/<int:id>/edit', methods=['GET'])
# def edit_entry(id):
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     entry = Entry.query.get(id)
#     return render_template('entries/edit.html', entry=entry)


# @app.route('/entries/<int:id>/update', methods=['POST'])
# def update_entry(id):
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     entry = Entry.query.get(id)
#     entry.title = request.form['title']
#     entry.text = request.form['text']
#     db.session.merge(entry)
#     db.session.commit()
#     flash('記事が更新されました')
#     return redirect(url_for('show_entries'))
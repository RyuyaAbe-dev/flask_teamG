from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from datetime import date

@app.route("/maintenance_date", methods=["POST"])
def maintenance_date():
    #입력 받은 공휴일의 날짜 형식을 변환
    dt = date(int(request.form["holiday"][0:4]), int(request.form["holiday"][5:7]), int(request.form["holiday"][8:10]))
    if request.form["button"] == "insert_update":
        #DB데이터를 취득
        holiday = Holiday.query.filter_by(holi_date=dt).first()
        
        #DB에 데이터가 없으면 새로운 데이터를 추가
        if holiday is None:
            holiday_insert = Holiday(holi_date = dt, holi_text = request.form["holiday_text"])
            db.session.add(holiday_insert)
            db.session.commit()
            #메세지를 변수에 저장
            msg_out = request.form["holiday"] + "(" + request.form["holiday_text"] + ") が登録されました"
        # DB에 데이터가 있으면 데이터를 업데이트
        else:
            holiday_insert = Holiday(holi_date = holiday.holi_date, holi_text = request.form["holiday_text"])
            session.merge(holiday_insert)
            session.commit()
            #메세지를 변수에 저장
            msg_out = request.form["holiday"] + "は「" + request.form["holiday_text"] + "」 に更新されました"
            
        return render_template("result.html", msg=msg_out)
    
    elif request.form["button"] == "delete":
        holiday = Holiday.query.filter_by(holi_date=dt).first()
        #DB에 데이터가 있으면 데이터를 삭제
        if holiday is None:
            flash(request.form["holiday"] + "は、祝日マスタに登録されていません")
            return redirect(url_for("input"))
        else:
            Holiday.query.filter_by(holi_date=dt).delete()
            db.session.commit()
            msg_out = str(holiday.holi_date) + "(" + holiday.holi_text + ") は、削除されました"
            return render_template("result.html", msg=msg_out)
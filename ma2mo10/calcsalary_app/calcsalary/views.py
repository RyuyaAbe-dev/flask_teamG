from flask import request, render_template, flash, redirect, url_for, session
from decimal import Decimal, ROUND_HALF_UP
from calcsalary import app

@app.route('/')
# リクエストがあった時の処理  ラッパーに渡す
def show_input():
    # トップページに遷移
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def calcsalary():
    MAX_INPUT = 9999999999                           # 入力できる上限値
    MILLION = 1000000                                # 100万円
    total_salary = 0                                 # 給与
    tax = 0                                          # 税額
    salary = 0                                       # 支給額
    # 給与の計算
    if request.method == 'POST':
        # 給与が入力されていないとき
        if request.form['salary'] == '':
            flash('給与が未入力です。入力してください。')
            return redirect(url_for('show_input'))
        # 入力が10桁より大きかったとき
        elif int(request.form['salary']) > MAX_INPUT:
            flash('給与には最大9,999,999,999まで入力可能です。')
            session['input_data'] = int(request.form['salary'])
            return redirect(url_for('show_input'))
        # マイナスの値が入力されたとき
        elif int(request.form['salary']) < 0:
            flash('給与にはマイナスの値は入力できません。')
            session['input_data'] = int(request.form['salary'])
            return redirect(url_for('show_input'))
        else:
            # 入力値を代入
            total_salary = int(request.form['salary'])
            session['input_data'] = total_salary       
            if total_salary > MILLION:
                tax = int(Decimal(str((total_salary - MILLION) * 0.2)) + Decimal(str(MILLION * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
            else:
                tax = int(Decimal(str(total_salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

            salary = int(total_salary - tax)
        # output.htmlに遷移して計算結果を渡す
        return render_template("output.html", salary_text = "給与：{0}円の場合、支給額:{1}円、税額:{2}円".format(total_salary, salary, tax))

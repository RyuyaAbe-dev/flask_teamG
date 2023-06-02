from flask import request, render_template
from decimal import Decimal, ROUND_HALF_UP
from calcsalary import app

@app.route('/')
# リクエストがあった時の処理  ラッパーに渡す
def show_input():
    # トップページに遷移
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def calcsalary():
    MILLION = 1000000
    total_salary = int(request.form['salary'])            #給与
    tax = 0                                          #税額
    salary = 0                                       #支給額
    # 給与の計算
    if request.method == 'POST':
        if total_salary > MILLION:
            tax = int(Decimal(str((total_salary - MILLION) * 0.2)) + Decimal(str(MILLION * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
        else:
            tax = int(Decimal(str(total_salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

        salary = int(total_salary - tax)
    # output.htmlに遷移して計算結果を渡す
    return render_template("output.html", salary_text = "給与：{0}円の場合、支給額:{1}円、税額:{2}円".format(total_salary, salary, tax))

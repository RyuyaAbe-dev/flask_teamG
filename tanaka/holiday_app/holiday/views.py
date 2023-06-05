from flask import request, redirect,url_for, render_template,flash,session
from holiday import app


@app.route('/')
def show_entries():
    return  render_template('entries/index.html')

@app.route('/result', methods=['GET', 'POST'])
def input_salary():
    if request.method == 'POST':
        input_salary = (request.form['salary'])
        if input_salary == "":
            flash('給与が未入力です。入力してください。（笑）')
            return render_template('entries/index.html')
        elif len(input_salary) > 10:
            flash('給与には最大9,999,999,999まで入力可能です。（笑）')
            return render_template('entries/index.html')
        elif int(input_salary) < 0:
            flash('給与にはマイナスの値は入力できません。（笑）')
            return render_template('entries/index.html')
        else:
            input_salary = int(input_salary)
            if input_salary > 1000000:
                # 100万円を超える部分を変数に代入
                under_million = input_salary - 1000000
                # 100万以下は税率10%、100万円を超える部分は税率20%で税額を計算
                tax_amount = 1000000 * 0.1 + under_million * 0.2
                # 小数第1位を四捨五入
                tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
                # 給与から税額を引き、支給額を計算
                payment = int(input_salary - tax_amount)
            # 給与が100万円以下の場合
            else:
                # 税率10%で税額を計算
                tax_amount = input_salary * 0.1
                # 小数第1位を四捨五入
                tax_amount = Decimal(str(tax_amount)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
                # 給与から税額を引き、支給額を計算
                payment = int(input_salary - tax_amount)
                return render_template("result.html", salary = "{:,}".format(input_salary),payment = "{:,}".format(payment), tax_amount="{:,}".format(tax_amount))
    else:
        return redirect('/')
    return render_template('result.html')

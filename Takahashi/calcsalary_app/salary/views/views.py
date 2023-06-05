from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def hello_world():
    return render_template('input.html')

@app.route('/output', methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        salary = int(request.form['salary'])
        if int(request.form['salary']) < 0:
            flash('エラー')
            return render_template('input.html')
        if salary > 1000000:
            tax = 100000 + (salary-1000000)*0.2
            tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) 
            pay_amount = salary - tax
        else:
            tax = salary * 0.1
            tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) 
            pay_amount = salary - tax

    return render_template('output.html', salary = salary, pay_amount = pay_amount, tax = tax)
        

@app.route("/input", methods=["GET"])
def input_page():
    return render_template("input.html")




 
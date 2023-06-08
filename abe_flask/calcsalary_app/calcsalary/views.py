from flask import render_template, request, redirect, url_for, Flask, flash
import math
from calcsalary import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    tax_rate = 0
    if request.method == 'POST':
        if request.form.get('salary') == '':
            flash('給与を入力してください')
            return render_template('index.html')
        if len(request.form.get('salary')) > 10:
            flash('給与には最大9999999999が入力可能です')
            return render_template('index.html')
        salary = int(request.form.get('salary'))
        if salary<0:
            flash('マイナスの値は入力できません')
            return render_template('index.html')
        if (salary < 1000000):
            tax_rate = 0.1
            tax = salary*tax_rate
            payment = salary - tax
            return render_template('output.html',salary = salary,payment = math.floor(payment), tax= math.floor(tax))
        else:
            tax_rate = 0.1
            tmp = salary - 1000000
            tax = 1000000 * tax_rate
            tax = tax + tmp * 0.2
            payment = salary - tax
            return render_template('output.html',salary = salary,payment = math.floor(payment), tax= math.floor(tax))
            # return print(f'支給額:{math.floor(payment)}、税額:{math.floor(tax)}',end="")

from flask import render_template, request, redirect, url_for, Flask
import math
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    tax_rate = 0
    print(request.form)
    if request.method == 'POST':
        salary = int(request.form.get('salary'))
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

if __name__ == "__main__":
    app.run(debug=True)
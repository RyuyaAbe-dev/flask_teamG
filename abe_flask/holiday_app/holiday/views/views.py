from flask import render_template, request, redirect, url_for, Flask, flash
import math
from holiday import db
from holiday.models.mst_holiday import Holiday
from holiday import app

@app.route('/')
def index():
    holidays = Holiday.query.all()
    print(holidays)
    return render_template('input.html')
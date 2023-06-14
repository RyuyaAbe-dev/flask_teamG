from spl_app import app
from flask import request, redirect, url_for, render_template, flash, session
import requests
from datetime import datetime

@app.route('/')
def show_index():
    nawabari_url = 'https://spla3.yuu26.com/api/regular/now'
    nawabari_now = requests.get(nawabari_url).json()
    charenge_url = 'https://spla3.yuu26.com/api/bankara-challenge/now'
    charenge_now = requests.get(charenge_url).json()
    open_url = 'https://spla3.yuu26.com/api/bankara-open/now'
    open_now = requests.get(open_url).json()
    x_url = 'https://spla3.yuu26.com/api/x/now'
    x_now = requests.get(x_url).json()

    return render_template('index.html', nawabari_now=nawabari_now, charenge_now=charenge_now, open_now=open_now, x_now=x_now)

@app.route('/schedule')
def show_schedule():
    schedule_url = 'https://spla3.yuu26.com/api/schedule'
    schedule = requests.get(schedule_url).json()

    nawabari_schedule = schedule['result']['regular']
    charenge_schedule = schedule['result']['bankara_challenge']
    open_schedule = schedule['result']['bankara_open']
    x_schedule = schedule['result']['x']

    return render_template('schedule.html', nawabari_schedule=nawabari_schedule, charenge_schedule=charenge_schedule, open_schedule=open_schedule, x_schedule=x_schedule)
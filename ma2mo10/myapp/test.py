import requests
import json
from datetime import datetime
def show_index():
    nawabari_url = 'https://spla3.yuu26.com/api/regular/now'
    nawabari_now = requests.get(nawabari_url).json()
    charenge_url = 'https://spla3.yuu26.com/api/bankara-challenge/now'
    charenge_now = requests.get(charenge_url).json()
    open_url = 'https://spla3.yuu26.com/api/bankara-open/now'
    open_now = requests.get(open_url).json()
    x_url = 'https://spla3.yuu26.com/api/x/now'
    x_now = requests.get(x_url).json()

    schedule_url = 'https://spla3.yuu26.com/api/schedule'
    schedule = requests.get(schedule_url).json()
    
    #nawabari_now_dict = json.load(nawabari_now_json)
    print(schedule['result']['regular'][0]['start_time'])

show_index()
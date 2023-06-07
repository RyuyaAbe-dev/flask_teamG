# 事前にrequestsをインポートしておく
import requests
import csv
from flask import Flask
app = Flask(__name__)
from pokemon_app import db
from pokemon_app.models.tables import Pokemon
filename = 'data/pokemon_data.csv'
import random

pokemon_list = []
csv_header = ""
with open(filename, encoding='utf-8_sig', newline='') as f:
    csvreader = csv.reader(f)
    pokemon_dict = {}
    for i,row in enumerate(csvreader):
        if i == 0:
            csv_header = row
        description = ""
        # if i > 4:
        #     break
        if i < 300:
            url = f'https://pokeapi.co/api/v2/pokemon-species/{i}'
            response = requests.get(url)
            # GETリクエストでデータを取得し、JSON形式に変える
            if 'json' in response.headers.get('content-type'):
                print(f'{i}番目')
                result = response.json()
                pokemon_data = response.json()
                texts = pokemon_data['flavor_text_entries']
                for i in range(len(texts)):
                    if pokemon_data['flavor_text_entries'][i]['language']['name'] == 'ja':
                        description = pokemon_data['flavor_text_entries'][i]['flavor_text']
                        print(description)
                        break
        for k,h in enumerate(csv_header):
            pokemon_dict[h] = row[k]
            pokemon_dict['説明'] = description
            description = ""
        pokemon_list.append(pokemon_dict)
        pokemon_dict={}
print(pokemon_list)


for i,pokemon in enumerate(pokemon_list):
    if i == 0:
        continue
    print(f'{i}番目')
    pokemons = Pokemon(
        name = pokemon['名前'],
        description = pokemon['説明'],
        image = pokemon['画像URL'],
        height = float(pokemon['高さ']),
        weight = float(pokemon['重さ']),
        status = float(pokemon['ステータス']),
        hp = float(pokemon['HP']),
        attack = float(pokemon['こうげき']),
        defence = float(pokemon['ぼうぎょ']),
        special_attack = float(pokemon['とくこう']),
        special_defence = float(pokemon['とくぼう']),
        speed = float(pokemon['すばやさ']),
        legend = pokemon['伝説'],
        catch_rate = float(pokemon['捕まえやすさ'])
    )
    db.session.add(pokemons)
    db.session.commit()
# フシギダネ（No.1）の基本情報を取得するエンドポイント（URL）
# url = "https://pokeapi.co/api/v2/pokemon-species/1"

# # GETリクエストでデータを取得し、JSON形式に変える
# response = requests.get(url)
# pokemon_data = response.json()

# # データを見る
# print(pokemon_data['names'][0]['name'])
# print()
# print(pokemon_data['genera'][0]['genus'])
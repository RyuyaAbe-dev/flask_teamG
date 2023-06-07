# 事前にrequestsをインポートしておく
import requests
import csv
filename = 'csv/pokemon_data.csv'
from pokemon_app import db
from pokemon_app.models.tables import Item
import random

# for i in range(10):
#     items = Item(
#         name=f'アイテム{random.randint(0,1000)}', 
#         description='textが入ります', 
#         image=f'https://picsum.photos/200/300?random={random.randint(0,2000)}',
#         stock=random.randint(0,200),
#         price=random.randint(0,2000)
#     )
#     db.session.add(items)
#     db.session.commit()
csv_header = ""
with open(filename, encoding='utf-8_sig', newline='') as f:
    csvreader = csv.reader(f)
    for i,row in enumerate(csvreader):
        if i == 0:
            csv_header = row
print(csv_header)
# # フシギダネ（No.1）の基本情報を取得するエンドポイント（URL）
# url = "https://pokeapi.co/api/v2/pokemon-species/1"

# # GETリクエストでデータを取得し、JSON形式に変える
# response = requests.get(url)
# pokemon_data = response.json()

# # データを見る
# print(pokemon_data['names'][0]['name'])
# print(pokemon_data['flavor_text_entries'][29]['flavor_text'])
# print(pokemon_data['genera'][0]['genus'])
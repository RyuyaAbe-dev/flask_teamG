from pokemon_app import db
from pokemon_app.models.tables import Pokemon
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
from flask import Flask, jsonify

app = Flask(__name__)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [
    Item("Intel Core i5-11600K", 100),
    Item("Intel Core i7-11700K", 200),
    Item("Intel Core i9-11900K", 300),
    Item("AMD Ryzen 5 5600X", 150),
    Item("AMD Ryzen 7 5800X", 250),
    Item("AMD Ryzen 9 5900X", 350),
]

@app.route('/items')
def get_items():
    items_list = []
    for item in items:
        item_dict = {
            "name": item.name,
            "price": item.price
        }
        items_list.append(item_dict)
    return jsonify(items_list)

if __name__ == '__main__':
    app.run()

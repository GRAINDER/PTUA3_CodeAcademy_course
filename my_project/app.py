from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['restaurant']
table_collection = db['tables']
order_collection = db['orders']

@app.route('/')
def index():
    tables = table_collection.find()
    return render_template('index.html', tables=tables)

@app.route('/reserve/<table_id>', methods=['POST'])
def reserve(table_id):
    table_collection.update_one({'_id': table_id}, {'$set': {'reserved': True}})
    return redirect('/')

@app.route('/order/<table_id>', methods=['POST'])
def order(table_id):
    table = table_collection.find_one({'_id': table_id})
    food = request.form.get('food')
    drinks = request.form.get('drinks')
    order = {
        'table_id': table_id,
        'table_number': table['number'],
        'food': food,
        'drinks': drinks,
        'timestamp': datetime.datetime.now()
    }
    order_collection.insert_one(order)
    return redirect('/')

@app.route('/receipt/<order_id>')
def receipt(order_id):
    order = order_collection.find_one({'_id': order_id})
    return render_template('receipt.html', order=order)

if __name__ == '__main__':
    app.run(debug=True)

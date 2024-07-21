from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def read_csv(file_path):
    data = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

def read_sql(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
    conn.close()
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sql('products.db')
    else:
        error = 'Wrong source specified. Please use "json", "csv", or "sql".'

    if not error and product_id:
        product_id = int(product_id)
        products = [product for product in products if product['id'] == product_id]
        if not products:
            error = 'Product not found.'

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

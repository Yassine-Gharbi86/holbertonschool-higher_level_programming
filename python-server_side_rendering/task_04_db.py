from flask import Flask, render_template, request, json
import csv
import sqlite3

app = Flask(__name__)

# Load data from JSON
def load_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return None

# Load data from CSV
def load_csv_data():
    try:
        products = []
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None

# Load data from SQLite
def load_sql_data(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
        return products
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        data = load_json_data()
    elif source == "csv":
        data = load_csv_data()
    elif source == "sql":
        data = load_sql_data(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if data is None:
        return render_template('product_display.html', error="Error loading data")

    if product_id and not data:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

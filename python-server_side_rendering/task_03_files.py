from flask import Flask, render_template, request, json
import csv

app = Flask(__name__)

def load_json_data():
    """Load product data from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        return None

def load_csv_data():
    """Load product data from CSV file."""
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
    except Exception as e:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Load data based on the source
    if source == "json":
        data = load_json_data()
    elif source == "csv":
        data = load_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    if data is None:
        return render_template('product_display.html', error="Error loading data")

    # Filter by product ID if provided
    if product_id:
        filtered_data = [p for p in data if p["id"] == product_id]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

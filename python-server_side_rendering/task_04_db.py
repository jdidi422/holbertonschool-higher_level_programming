import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def load_json_data():
    """Load product data from JSON file."""
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_csv_data():
    """Load product data from CSV file."""
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            return [{"id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"])} for row in reader]
    except (FileNotFoundError, csv.Error, ValueError):
        return []

def load_sql_data():
    """Load product data from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        product_list = load_json_data()
    elif source == "csv":
        product_list = load_csv_data()
    elif source == "sql":
        product_list = load_sql_data()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json', 'csv', or 'sql'.")

    if product_id:
        filtered_product = next((p for p in product_list if p["id"] == product_id), None)
        if not filtered_product:
            return render_template("product_display.html", error="Product not found.")
        product_list = [filtered_product]

    return render_template("product_display.html", products=product_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
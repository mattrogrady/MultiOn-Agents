from flask import Flask, render_template, request, jsonify
from multion.client import MultiOn
from browse_products import browse_amazon
import time

app = Flask(__name__)
client = MultiOn(api_key="105ae8bf8848469e9fdf0efcba4c9688")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    scrape_task = request.json['url']
    retrieve_response = client.retrieve(
        url=scrape_task,
        cmd="Get all items and their name, price, and purchase url.",
        fields=["name", "price", "purchase_url"],
        render_js=True,
        scroll_to_bottom=True,
        max_items=5
    )
    data = retrieve_response.data
    return jsonify(data)

@app.route('/browse_amazon', methods=['POST'])
def browse_amazon_route():
    product_name = request.json['product_name']
    product_price = request.json['product_price']
    time.sleep(5)  # Simulate a delay for browsing
    browse_amazon(product_name, product_price)
    return jsonify({"status": "done"})

if __name__ == '__main__':
    app.run(debug=True)

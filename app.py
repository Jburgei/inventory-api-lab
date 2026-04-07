from flask import Flask, jsonify, request
from data import inventory
from services import fetch_product_by_barcode

app = Flask(__name__)


@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)


@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data or "stock" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_id = len(inventory) + 1

    new_item = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_inventory_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for item in inventory:
        if item["id"] == item_id:
            if "name" in data:
                item["name"] = data["name"]
            if "price" in data:
                item["price"] = data["price"]
            if "stock" in data:
                item["stock"] = data["stock"]

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return '', 204

    return jsonify({"error": "Item not found"}), 404


@app.route('/external/barcode/<barcode>', methods=['GET'])
def get_external_product(barcode):
    product = fetch_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    if "error" in product:
        return jsonify(product), 502

    return jsonify(product), 200


if __name__ == '__main__':
    app.run(debug=True)
from flask import Blueprint, jsonify, current_app, request
from datetime import datetime
from flask_jwt_extended import jwt_required
from helpers.validation_helper import ValidationHelper
from models.inventory_model import Inventory

inventory_controller = Blueprint('inventory_controller', __name__)

@inventory_controller.route('/inventory', methods=['GET'])
@jwt_required()
def list_inventory():
    cur = current_app.mysql.connection.cursor()
    cur.execute("SELECT * FROM inventory")
    rv = cur.fetchall()
    cur.close()
    inventory = []
    for row in rv:
        inventory.append({
            "ID": row[0],
            "item_name": row[1],
            "category": row[2],
            "quantity": row[3],
            "unit_price": float(row[4]),
            "supplier": row[5],
            "date_added": row[6],
            "last_update": row[7],
            "warning_limit": row[8],
            "location": row[9]
        })
    return jsonify(inventory)

@inventory_controller.route('/inventory/<int:id>', methods=['GET'])
def get_one(id):
    row = Inventory.get_by_id(id)
    inventory = {
        "ID": row[0],
        "item_name": row[1],
        "category": row[2],
        "quantity": row[3],
        "unit_price": float(row[4]),
        "supplier": row[5],
        "date_added": row[6],
        "last_update": row[7],
        "warning_limit": row[8],
        "location": row[9]
    }

    return inventory, 200

@inventory_controller.route('/inventory', methods=['POST'])
@jwt_required()
def add_inventory():
    requestData = request.get_json()
    
    validationRules = {
        "item_name": "required",
        "quantity": "required",
        "unit_price": "required",
        "supplier": "required",
        "category": "required",
        "location": "required",
    }
    isError, validationData = ValidationHelper.validate_data(requestData, validationRules)

    if isError:
        return {"errors": validationData}, 400
    
    # check if item already exists
    cursor = current_app.mysql.connection.cursor()
    cursor.execute("SELECT * FROM inventory WHERE item_name = %s", (requestData.get('item_name'),))
    item = cursor.fetchone()
    if item:
        return jsonify({'message': 'Inventory item already exists'}), 409

    # insert data
    inventory = Inventory( 
        item_name = requestData.get('item_name'),
        category = requestData.get('category', None),
        quantity = requestData.get('quantity', 0),
        unit_price = requestData.get('unit_price', 0),
        supplier = requestData.get('supplier', None),
        date_added = datetime.now(),
        warning_limit = requestData.get('warning_limit', 0),
        location = requestData.get('location', None)
    )
    inventory.create()

    return jsonify({'message': 'Inventory item added successfully'}), 201


@inventory_controller.route('/inventory/set-limit/<int:id>', methods=['POST'])
@jwt_required()
def set_limit(id):
    # set inventory limit
    requestData = request.get_json()
    if requestData.get('limit') is None:
        return jsonify({'errors': 'limit is required'}), 400
    if int(requestData.get('limit')) <= 0:
        return jsonify({'errors': 'limit must be greater than 0'}), 400

    Inventory.set_limit(id, requestData.get('limit', 5))
    return jsonify({'message': 'set limit successfully'}), 200

@inventory_controller.route('/inventory/<int:id>', methods=['PUT'])
@jwt_required()
def update_inventory(id):
    requestData = request.get_json()
    
    inventory = Inventory(
        item_name=requestData.get('item_name', None),
        category=requestData.get('category', None),
        quantity=requestData.get('quantity', 0),
        unit_price=requestData.get('unit_price', 0),
        supplier=requestData.get('supplier', None),
        last_update=datetime.now(),
        warning_limit=requestData.get('warning_limit', 5),
        location=requestData.get('location', None)
    );
    inventory.update(id)
    return jsonify({'message': 'Inventory item updated successfully'})

@inventory_controller.route('/inventory/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_inventory(id):
    Inventory.delete(id)
    return jsonify({'message': 'Inventory item deleted successfully'}), 200

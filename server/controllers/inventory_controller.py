from flask import Blueprint, jsonify, current_app, request
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from helpers.validation_helper import ValidationHelper
from models.inventory import Inventory
from models.db import db

inventory_controller = Blueprint('inventory_controller', __name__)

@inventory_controller.route('/inventory', methods=['GET'])
@jwt_required()
def list_inventory():
    inventories = Inventory.query.filter_by(user_id=get_jwt_identity()).all()
    inventories = [inv.to_dict() for inv in inventories]
    return inventories, 200

@inventory_controller.route('/inventory/<int:id>', methods=['GET'])
def get_one(id):
    inventory = Inventory.query.filter_by(id=id).first()
    
    if not inventory:
        return jsonify({'message': 'Inventory item not found'}), 404
    
    return inventory.to_dict(), 200

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
        "location": "required"
    }
    isError, validationData = ValidationHelper.validate_data(requestData, validationRules)

    if isError:
        return {"errors": validationData}, 400
    
    # check if item already exists
    item = Inventory.query.filter_by(item_name=requestData.get('item_name')).first()
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
        location = requestData.get('location', None),
        user_id = get_jwt_identity()
    )
    db.session.add(inventory)
    db.session.commit()

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

    inventory = Inventory.query.get(id)
    
    if inventory:
        inventory.warning_limit = requestData.get('limit', 5)
        db.session.add(inventory)
        db.session.commit()
        return jsonify({'message': 'set limit successfully'}), 200

    return jsonify({'message': 'Inventory item not found'}), 404

@inventory_controller.route('/inventory/<int:id>', methods=['PUT'])
@jwt_required()
def update_inventory(id):
    requestData = request.get_json()
    
    inventory = Inventory.query.get(id)

    if inventory:
        inventory.item_name = requestData.get('item_name', None)
        inventory.category = requestData.get('category', None)
        inventory.quantity = requestData.get('quantity', 0)
        inventory.unit_price = requestData.get('unit_price', 0)
        inventory.supplier = requestData.get('supplier', None)
        inventory.last_update = datetime.now()
        inventory.warning_limit = requestData.get('warning_limit', 5)
        inventory.location = requestData.get('location', None)

        db.session.add(inventory)
        db.session.commit()

        return jsonify({'message': 'Inventory item updated successfully'})

    return jsonify({'message': 'Inventory item not found'}), 404

@inventory_controller.route('/inventory/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_inventory(id):
    inventory = Inventory.query.get(id)

    if inventory:
        db.session.delete(inventory)
        db.session.commit()

        return jsonify({'message': 'Inventory item deleted successfully'}), 200
    return jsonify({'message': 'Inventory item not found'}), 404

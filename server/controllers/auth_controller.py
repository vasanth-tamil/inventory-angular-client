import hashlib
from datetime import datetime
from flask import Blueprint, request, current_app
from sqlalchemy import and_
from flask_jwt_extended import create_access_token, jwt_required
from helpers.validation_helper import ValidationHelper
from models.user import User
from models.db import db

auth_controller = Blueprint('auth_controller', __name__, url_prefix="/auth")

@auth_controller.route('/sign-up', methods=['POST'])
def sign_up():
    requestData = request.get_json()

    # validations
    validationRules = {
        "email": "required",
        "password": "required",
        "re_password": "required",
    }
    isError, validationData = ValidationHelper.validate_data(requestData, validationRules)

    if isError:
        return {"errors": validationData}, 400

    # password and re_password is same or  not check 
    if requestData.get('password') != requestData.get('re_password') :
        return {"errors": "Password does not match"}, 400

    # email already exists
    user = User.query.filter_by(email=requestData.get('email')).first()
    if user:
        return {'errors': 'User already exists'}, 409
    
    # create user
    requestData['password'] = hashlib.sha256(requestData.get('password').encode('utf-8')).hexdigest()
    user = User(name=requestData.get('name'), email=requestData.get('email'), password=requestData.get('password'))
    db.session.add(user)
    db.session.commit()

    return {"message": "User created successfully"}, 201

@auth_controller.route('/sign-in', methods=['POST'])
def sign_in():
    requestData = request.get_json()
    
    validationRules = {
        "email": "required",
        "password": "required"
    }
    isError, validationData = ValidationHelper.validate_data(requestData, validationRules)
    if isError:
        return {"errors": validationData}, 400
    
    # get user by email and password
    requestData['password'] = hashlib.sha256(requestData.get('password').encode('utf-8')).hexdigest()
    user = User.query.filter_by(email=requestData.get('email')).first()

    if user:
        # check password
        if user.password != requestData.get('password'):
            return {"message": "invalid credentials"}, 401

        access_token = create_access_token(identity=user.id)
        return {"message": "User logged in successfully", "token": access_token}, 200
    return {"message": "invalid credentials"}, 401

@auth_controller.route('/sign-out', methods=['GET'])
@jwt_required()
def sign_out():
    return {"message": "User signed out successfully"}, 200
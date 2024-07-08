import hashlib
from datetime import datetime
from flask import Blueprint, request, current_app
from flask_jwt_extended import create_access_token, jwt_required
from helpers.validation_helper import ValidationHelper
from models.user_model import User

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
    user = User.email_exists(requestData.get('email'))
    if user:
        return {'errors': 'User already exists'}, 409
    
    # create user
    user = User(requestData.get('name'), requestData.get('email'), requestData.get('password'))
    user.create()

    return {"message": "User created successfully"}, 201

@auth_controller.route('/sign-in', methods=['POST'])
def sign_in():
    user = request.get_json()
    
    validationRules = {
        "email": "required",
        "password": "required"
    }
    isError, validationData = ValidationHelper.validate_data(user, validationRules)
    if isError:
        return {"errors": validationData}, 400
    
    # get user by email and password
    user = User.get_user_by_email_and_password(user.get('email'), user.get('password'))

    if user:
        access_token = create_access_token(identity=user[0])
        return {"message": "User logged in successfully", "token": access_token}, 200
    return {"message": "invalid credentials"}, 401

@auth_controller.route('/sign-out', methods=['GET'])
@jwt_required()
def sign_out():
    return {"message": "User signed out successfully"}, 200
from datetime import timedelta
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

from controllers.auth_controller import auth_controller
from controllers.inventory_controller import inventory_controller


def main():
    # load .env file
    load_dotenv() 

    # start the server
    app = Flask(__name__)

    with app.app_context():
        app = Flask(__name__)
        #  MYSQL Configurations
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = ''
        app.config['MYSQL_DB'] = 'inventory_database'
        app.mysql = MySQL(app)
        print("Connected to MySQL")

        # JWT Authentication Configuration
        app.config['SECRET_KEY'] = 's3cr3t'
        app.config["JWT_SECRET_KEY"] = 's3cr3t'
        app.config['JWT_TOKEN_LOCATION'] = ['headers']
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=30) 
        jwt = JWTManager(app)
        print("JWT Authentication Configured")

    # controll and route blueprint registration
    app.register_blueprint(auth_controller)
    app.register_blueprint(inventory_controller)
    cors = CORS(app) # allow cross-origin requests

    @app.errorhandler(403)
    def forbidden(e):
        return jsonify({
            "message": "Forbidden",
            "error": str(e),
            "data": None
        }), 403

    @app.errorhandler(404)
    def forbidden(e):
        return jsonify({
            "message": "Endpoint Not Found",
            "error": str(e),
            "data": None
        }), 404


    # run the server
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == '__main__':
    main()
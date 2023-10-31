# we invoke the necessary libraries
from flask import Flask, jsonify
# from config import config
from flask_cors import CORS, cross_origin
import controller
from db import get_db_connection

# The access point is created
server = Flask(__name__)

#this allow recurser exchange
CORS(server)




# The route to enter the service is created.
@cross_origin
@server.get('/vehicles')
def index():
    config = get_db_connection()
    if config:
        try:
            return controller.stock(config)
        except Exception as ex:
                return jsonify({'message': ex})
    else:
        return jsonify({'message': 'Error connecting to the database'})


@cross_origin
# The path displaying unit information is created.
@server.get('/vehicle/<string:id>')
def get_vehicle(id):
    config = get_db_connection()
    try:
       return controller.vehicle(config, id)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new vehicle is created.
@server.post('/vehicle')
def create_vehicle():
    config = get_db_connection()
    try:
        return controller.create_vehicle(config)
    except Exception as ex:
        return jsonify({'message': ex})


@cross_origin
# The route to create a new stock is created.
@server.post('/stock')
def create_stock():
    config = get_db_connection()
    try:
        return controller.create_stock(config)
    except Exception as ex:
        return jsonify({'message': ex})


@cross_origin
# The route is created to remove the stock
@server.delete("/stock/<string:id>")
def delete_stock(id):
    config = get_db_connection()
    try:
        return controller.delete_stock(config, id)
    except Exception as ex:
        return jsonify({'message': ex})


# A function is created to show when a page is not found.

# the application is executed
if __name__ == '__main__':
    server.run(debug=True)
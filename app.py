# we invoke the necessary libraries
from flask import Flask, jsonify
# from config import config
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import controller

# The access point is created
server = Flask(__name__)

#this allow recurser exchange
CORS(server)

# The connection point to the base is created.
server.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
server.config['MYSQL_USER'] = 'bee0e9755133d2'
server.config['MYSQL_PASSWORD'] = 'f3e9360a'
server.config['MYSQL_DB'] = 'heroku_23edc9681868d22'
mysql = MySQL(server)


# The route to enter the service is created.
@cross_origin
@server.get('/vehicles')
def index():
    try:
        return controller.stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


@cross_origin
# The path displaying unit information is created.
@server.get('/vehicle/<int:id>')
def get_vehicle(id):
    try:
       return controller.vehicle(mysql, id)
    except Exception as ex:
        return jsonify({'message': ex})


# The route to create a new vehicle is created.
@server.post('/vehicle')
def create_vehicle():
    try:
        return controller.create_vehicle(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


@cross_origin
# The route to create a new stock is created.
@server.post('/stock')
def create_stock():
    try:
        return controller.create_stock(mysql)
    except Exception as ex:
        return jsonify({'message': ex})


@cross_origin
# The route is created to remove the stock
@server.delete("/stock/<string:id>")
def delete_stock(id):
    try:
        return controller.delete_stock(mysql, id)
    except Exception as ex:
        return jsonify({'message': ex})


# A function is created to show when a page is not found.

# the application is executed
if __name__ == '__main__':
    server.run(debug=True)
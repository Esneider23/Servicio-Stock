from flask import jsonify, request, json


# the function that allows to list all vehicles in stock is created
def stock(mysql):
    cursor = mysql.connection.cursor()
    sql = "select v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security " \
          "from stock s " \
          "inner join vehicle v on (s.name = v.id) inner join supplier su on (s.supplier = su.idsupplier)"
    cursor.execute(sql)
    data = cursor.fetchall()
    vehicles = []
    for fila in data:
        vehicle = {'name': fila[0], 'supplier': fila[1], 'price': fila[2], 'motor': fila[3], 'gearbox': fila[4],
                   'security': fila[5]}
        vehicles.append(vehicle)
    return jsonify({'vehicles': vehicles, 'message': 'Listed vehicles'})


# the function allowing to list the information of a particular vehicle is created
def vehicle(mysql, id):
    cursor = mysql.connection.cursor()
    sql = "select v.id, v.name, su.name, s.selling_price, v.motor, v.gearbox, v.security from stock s " \
          "inner join vehicle v on (s.name = v.id) inner join supplier su on (s.supplier = su.idsupplier) " \
          "where v.id = '{0}'".format(id)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data is not None:
        vehicle = {'name': data[0], 'supplier': data[1], 'price': data[2], 'motor': data[3], 'gearbox': data[4],
                   'security': data[5]}
        return jsonify({'vehicles': vehicle, 'message': 'Information on the vehicle found'})
    else:
        return jsonify({'message': 'Vehicle not found'})


# the function allowing the creation of a new vehicle is created
def create_vehicle(mysql):
    cursor = mysql.connection.cursor()
    sql = """insert into vehicle(name, motor, gearbox, security, type) values ('{0}', '{1}', '{2}',
            '{3}', '{4}') """.format(request.json['name'], request.json['motor'], request.json['gearbox'],
                                     request.json['security'], request.json['type'])
    cursor.execute(sql)
    mysql.connection.commit()
    return jsonify({'message': 'Vehicle created'})


# the function is created that allows a vehicle to be removed from stock
# the function that allows you to create a new stock is created
def create_stock(mysql):
    cursor = mysql.connection.cursor()
    sql = """insert into stock (name, supplier, selling_price, quantity) 
           values ('{0}', '{1}', '{2}', '{3}')""".format(request.json['name'], request.json['supplier'],
                                                         request.json['selling_price'], request.json['quantity'])
    cursor.execute(sql)
    mysql.connection.commit()
    return jsonify({'message': 'Stock update'})


# the function is created that allows a vehicle to be removed from stock
def delete_stock(mysql, id):
    sql = "delete from stock where idstock = '{0}'".format(id)
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    mysql.connection.commit()
    return jsonify({'message': "The stock was successfully removed"})

from flask import Flask,render_template,request,jsonify
# from bson.json_util import dumps
# from bson.objectid import ObjectId

app=Flask(__name__, template_folder='template')
app.secret_key='secretkey'
app.config['MONGO_URI']='mongodb://localhost:27017/School.Student'

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
#from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__, template_folder='template')
app.secret_key = 'secretkey'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/School'

mongo = PyMongo(app)

#Insert Operation

@app.route('/add', methods=['POST'])
def student():
    _json = request.json
    _name = _json['First_Name']
    _lastname = _json['Last_Name']
    _Class = _json['Class']
    _Roll_No = _json['Roll_No']
    _DOB = _json['DOB']

    if _name and _lastname and _Class and _DOB and _Roll_No and request.method == 'POST':

        id = mongo.db.Student.insert({'name': _name, 'lastname': _lastname, 'DOB': _DOB, 'Class': _Class, 'Roll_No': _Roll_No})
        resp = jsonify("User added Successfully ")
        resp.status_code = 200
        return resp

    else:
        return not_found()

@app.route('/Student')
def users():
    users = mongo.db.Student.find()
    resp = dumps(users)
    return resp

@app.route('/Student/<id>')
def user(id):
    users = mongo.db.Student.find_one({"_id": ObjectId(id)})
    resp = dumps(users)
    return resp

#Delete Operation Based on id
@app.route('/delete/<id>', methods = ['DELETE'])
def delete_user(id):
    mongo.db.Student.delete_one({"_id": ObjectId(id)})
    resp = jsonify("User deleted Successfully ")
    resp.status_code  = 200
    return resp

#Update operation based on id
@app.route('/update/<id>', methods = ['PUT'])
def update_user(id):
    _id =id
    _json = request.json
    _name = _json['First_Name']
    _lastname = _json['Last_Name']
    _Class = _json['Class']
    _DOB = _json['DOB']
    _Roll_No = _json['Roll_No']

    if  _name and _lastname and _Class and _DOB and _Roll_No and request.method == 'PUT':
        mongo.db.Student.update_one({'_id' : ObjectId(id) if '$oid' in _id else ObjectId(id)}, {'$set' : {'name': _name, 'lastname': _lastname, 'DOB': _DOB, 'Class': _Class, 'Roll_No': _Roll_No} } )

        resp = jsonify(" User Update successfully ")
        resp.status_code = 200
        return resp

    else:
        return not_found



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found'+request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run(debug=True)







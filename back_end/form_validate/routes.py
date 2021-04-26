from form_validate import app, db
from flask import json, session, request, jsonify, Response
from form_validate.models.user import User, UserSchema
from flask_cors import cross_origin

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/login', methods=["POST", "GET"])
def login(): 
  if request.method == 'POST':
    username = dict(request.json)["username"]
    password = dict(request.json)["password"]

    user = User.find_by_username(username)
    if user != None and user.password == password:
      return jsonify(id=user.id, username=user.username, name=user.name)
    else:
      return jsonify({"error": "incorrect login"}), 401


@app.route('/new', methods=["POST","GET"])
def new():
  if request.method == "POST":
    username = dict(request.json)["username"]
    password = dict(request.json)["password"]
    name = dict(request.json)["name"]

    try:
      user = User(username=username, name=name, password=password)
      db.session.add(user)
      db.session.commit()
      return jsonify(id=user.id, username=user.username, name=user.name)
    except AssertionError as error:
      return jsonify(error=f'{error}'), 400

@app.route('/', methods=["GET"])
def index():
  users = User.query.all()
  result = users_schema.dump(users)
  # return jsonify(result.data)
  return jsonify(result)
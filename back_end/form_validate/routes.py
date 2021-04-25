from form_validate import app, db
from flask import json, session, request, jsonify, Response
from form_validate.models.user import User
from flask_cors import cross_origin
# from flask_login import current_user, login_required, logout_user


@app.route('/', methods=["POST", "GET"])
@cross_origin()
def index():
  print('test')
  print(request.json)
  print(dict(request.json)["username"])
  print(dict(request.json)["password"])
  username = dict(request.json)["username"]
  user = User.find_by_username(username)
  print(user)
  print(user == None)
  if user != None and user.password == request.json["password"]:
    return jsonify(id=user.id, username=user.username, password=user.password)
  else:
    return jsonify({"error": "could not find user"}), 422
    # return Response({"error": "could not find user"}, status=401, mimetype='application/json')#jsonify({"error": "could not find user"}), 401


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

    user = User.create(username=username, name=name, password=password)


@app.route('/logout')
def logout():
  # remove the username from the session if it's there
  session.pop('username', None)

from form_validate import app, db
from flask import json, session, request, jsonify, Response
from form_validate.models.user import User
from flask_cors import cross_origin

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


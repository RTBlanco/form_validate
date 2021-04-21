from form_validate import app, db
from flask import json, session, request, jsonify, Response
from form_validate.models.user import User
# from flask_login import current_user, login_required, logout_user


@app.route('/', methods=["POST", "GET"])
# @login_required
def index():
  print(request.json)
  print(dict(request.json)["username"])
  username = dict(request.json)["username"]
  # user = User.query.filter(User.username == username).first()
  user = User.find_by_username(username)
  print(user == None)
  if user == None:
    # return jsonify({"error": "could not find user"}), 401
    # return Response({"error": "could not find user"}, status=401, mimetype='application/json')#jsonify({"error": "could not find user"}), 401
  else:
    return jsonify(id=user.id, username=user.username, password=user.password)


@app.route('/login', methods=["POST", "GET"])
def login():
  if request.method == 'POST':
    username = dict(request.json)["username"]
    password = dict(request.json)["password"]

    user = User.find_by_username(username)
    if user != None and user.password == password:
      session['username'] = username
      return jsonify(id=user.id, username=user.username)
    else:
      return jsonify({"error": "incorrect login"}), 401



@app.route('/logout')
def logout():
  # remove the username from the session if it's there
  session.pop('username', None)

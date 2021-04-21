from form_validate import app, db
from flask import session, request
from form_validate.models.user import User
# from flask_login import current_user, login_required, logout_user


@app.route('/', methods=["POST", "GET"])
# @login_required
def index():
  print(request.json)
  print(dict(request.json)["username"])
  return "<h1>test</h1>"


@app.route('/login', methods=["POST", "GET"])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']


@app.route('/logout')
def logout():
  # remove the username from the session if it's there
  session.pop('username', None)

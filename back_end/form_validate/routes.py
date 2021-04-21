from form_validate import app, db
from flask import session, request

app.secret_key = "testing"

@app.route('/')
def index():
  return "<h1>test</h1>"


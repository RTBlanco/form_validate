from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = "testing"
db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)


from form_validate import routes
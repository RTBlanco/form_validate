from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.secret_key = "testing"
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# login_manager = LoginManager()
# login_manager.init_app(app)


from form_validate import routes

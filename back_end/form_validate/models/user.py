from form_validate import db
# from flask_login import UserMixin

# @login_manager.user_loader
# def load_user(user_id):
#   return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)
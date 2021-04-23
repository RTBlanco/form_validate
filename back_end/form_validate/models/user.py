from form_validate import db
# from flask_login import UserMixin

# @login_manager.user_loader
# def load_user(user_id):
#   return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)

  @classmethod
  def find_by_username(self, username):
    """ This locates the user by usernamee """
    return User.query.filter(User.username == username).first()

  def __repr__(self):
    return "User :{ username: " + self.username + ", password: " + self.password + "}" 
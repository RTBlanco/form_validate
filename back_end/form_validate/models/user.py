from form_validate import db
# from flask_login import UserMixin

# @login_manager.user_loader
# def load_user(user_id):
#   return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)

  @classmethod
  def find_by_username(self, username):
    """ This locates the user by usernamee """
    return User.query.filter(User.username == username).first()

  @db.validates('username')
  def validate_username(self, key, username):
    if not username:
      raise AssertionError('No username provided')

    if User.query.filter(User.username == username).first():
      raise AssertionError('Username is already in use')

    return username

  @db.validates('password')
  def vaidate_password(self, key, password):
    if not password:
      raise AssertionError('No username provided')

    return password

  @db.validates('name')
  def vaidate_name(self, key, name):
    print(name)
    if not name:
      raise AssertionError('No username provided')
    return name 


  def create(self, username, name, password):
    pass 

  def __repr__(self):
    return "User :{name: " + self.name + " username: " + self.username + ", password: " + self.password + "}" 
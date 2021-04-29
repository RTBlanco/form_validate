import json
from form_validate import db, ma

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)

  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

  @classmethod
  def find_by_username(self, username):
    """ This locates the user by usernamee """
    return User.query.filter(User.username == username).first()

  @db.validates('username')
  def validate_username(self, key, username):
    if not username or username == None or username == "":
      raise AssertionError('No username provided')

    if User.query.filter(User.username == username).first():
      raise AssertionError('Username is already in use')

    return username

  @db.validates('password')
  def vaidate_password(self, key, password):
    if not password or password == None or password == "":
      raise AssertionError('No password provided')

    return password

  @db.validates('name')
  def vaidate_name(self, key, name):
    if not name or name == None or name == "":
      raise AssertionError('No name provided')

    return name 


  def __repr__(self):
    return 'User :{ name: "' + self.name + '", username: "' + self.username + '", password: "' + self.password + '"}' 



# class UserSchema(ma.Schema):
#   class Meta:
#     fields = ("id", "username", "name")
class UserSchema(ma.SQLAlchemySchema):
  class Meta:
    model = User

  id = ma.auto_field()
  name = ma.auto_field()
  username = ma.auto_field()

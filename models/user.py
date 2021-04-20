from db import db

class UserModel(db.Model):
  """
  ============
  User's Table
  ============

  User table contains:
  * id: primary key
  * email: unique value
  * password: hashed value

  Public methods:
  1. save_to_db: saves the user to the database
  2. find_by_username: finds the user based on email(username)
  3. find_by_id: finds the user based on user id
  """
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String())
  password = db.Column(db.String())

  def __init__(self, email, password):
    self.email = email
    self.password = password

  # def __repr__(self):
  #   return '<id {}>'.format(self.id)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_username(cls, email): # username mapping
    """
    find_by_username: finds the user by their email\n
    :param email: unique email for user to be found\n
    `:returns: user`
    """
    return cls.query.filter_by(email = email).first()

  @classmethod
  def find_by_id(cls, _id): # userid mapping
    """
    find_by_id: finds the user by their id\n
    :param _id: unique email for user to be found\n
    `:returns: user`
    """
    return cls.query.filter_by(id = _id).first()
from db import db

class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String())
  password = db.Column(db.String())

  def __init__(self, email, password):
    self.email = email
    self.password = password

  def __repr__(self):
    return '<id {}>'.format(self.id)
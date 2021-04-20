from db import db

class UserModel(db.Model):
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
    return cls.query.filter_by(email = email).first()

  @classmethod
  def find_by_id(cls, _id): # userid mapping
    return cls.query.filter_by(id = _id).first()
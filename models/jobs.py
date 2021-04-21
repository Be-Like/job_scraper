from db import db


class JobModel(db.Model):
  """
  ============
  Job Postings
  ============
  Job postings scraped from various job boards using scrapy

  Job table contains:
  * id: primary key
  * title
  * description
  * company_name
  * salary
  * rating
  * number_of_ratings
  * location
  * source
  * url: unique value

  Public methods:
  """
  __tablename__ = 'jobs'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String())
  description = db.Column(db.String())
  company_name = db.Column(db.String())
  salary = db.Column(db.Float(precision = 2))
  rating = db.Column(db.Float(precision = 1))
  number = db.Column(db.Integer())
  location = db.Column(db.String())
  source = db.Column(db.String())
  url = db.Column(db.String(), unique = True)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

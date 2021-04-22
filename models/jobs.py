import enum
from db import db


class PostingSource(enum.Enum):
  INDEED = 1


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
  source = db.Column(db.Enum(PostingSource))
  url = db.Column(db.String(), unique = True)

  def __init__(self,title=None,description=None,company_name=None,salary=None,rating=None,number=None,location=None,source=None,url=None):
    self.title = title
    self.description = description
    self.company_name = company_name
    self.salary = salary
    self.rating = rating
    self.number = number
    self.location = location
    self.source = source
    self.url = url

  # def __repr__(self):
  #   return f"""
  #     title: {title}
  #     description: {description}
  #     company_name: {company_name}
  #     salary: {salary}
  #     rating: {rating}
  #     number: {number}
  #     location: {location}
  #     source: {source}
  #     url: {url}
  #   """

  def json(self):
    return { 'id': self.id, 'title': self.title, 'url': self.url }

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

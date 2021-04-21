from flask_restful import Resource, reqparse
from models.jobs import JobModel


class FetchJobs(Resource):
  """
  ====================================
  Fetches Job Postings from Job Boards
  ====================================

  Controller

  Uses scrapy to fetch job postings from various job boards
  """

  FetchJobs
from flask_restful import Resource, reqparse
from models.jobs import JobModel


class Job(Resource):
  def post(self):
    return {'message': 'Job created successfully.'}, 201
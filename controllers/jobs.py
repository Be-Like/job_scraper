from flask_restful import Resource, reqparse
from models.jobs import JobModel


class Job(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument(
    'jobTitle',
    type=str,
    required=True,
    help="This field cannot be left blank!"
  )

  def post(self):
    job = JobModel(
      title='test',
      url='testing-again'
    )

    try:
      job.save_to_db()
    except:
      {'message': 'there was an error'}

    return job.json(), 201
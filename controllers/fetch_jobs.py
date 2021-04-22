from flask_restful import Resource, reqparse
from models.jobs import JobModel



import crochet
crochet.setup()
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time
from spiders.indeed_spider import IndeedSpider

crawl_runner = CrawlerRunner()
output_data = []

@crochet.run_in_reactor
def scrape():
  dispatcher.connect(_crawler_result, signal=signals.item_scraped)
  eventual = crawl_runner.crawl(IndeedSpider)
  return eventual

def _crawler_result(item, response, spider):
  job_title = item['job_title']
  job_description = item['job_description']
  rating = item['company_rating']
  numberOfRatings = item['number_of_ratings']
  url = item['ad_url']
  JobModel(
    title=job_title,
    description=job_description,
    # rating=rating
    # number_of_ratings=numberOfRatings,
    # source=1
    url=url
  ).save_to_db()

  print('hello world')
  output_data.append(dict(item))


class FetchJobs(Resource):
  """
  ====================================
  Fetches Job Postings from Job Boards
  ====================================

  Controller

  Uses scrapy to fetch job postings from various job boards
  """

  parser = reqparse.RequestParser()
  parser.add_argument(
    'jobTitle',
    type=str,
    required=True,
    help="This field cannot be left blank!"
  )

  def post(self):
    scrape()
    return {}, 200

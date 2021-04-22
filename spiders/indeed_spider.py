import scrapy

# from job_scraper.models.jobs import JobModel


class IndeedSpider(scrapy.Spider):
  name = 'indeed'

  start_urls = [
    'https://www.indeed.com/jobs?q=software+engineer&l=Remote&fromage=1'
  ]

  def parse(self, response):
    full_descriptions = response.css('a.jobtitle')
    for desc in full_descriptions:
      yield response.follow(desc, callback=self.parse_full_desc, cb_kwargs=dict(ad_url=desc.css('a::attr(href)').get(),))

  def parse_full_desc(self, response, ad_url=None):
    # job = JobModel(
    #   title=response.css('h1.jobsearch-JobInfoHeader-title::text').get(),
    #   description=response.css('div#jobDescriptionText *::text').getall(),
    #   rating=response.xpath('//meta[@itemprop="ratingValue"]/@content').extract_first(),
    #   number_of_ratings=response.xpath('//meta[@itemprop="ratingCount"]/@content').extract_first(),
    #   source=1,
    #   url=ad_url or 'N/A',
    # )

    # yield job.save_to_db()
    yield {
      'ad_url': ad_url,
      'job_title': response.css('h1.jobsearch-JobInfoHeader-title::text').get(),
      'company_rating': response.xpath('//meta[@itemprop="ratingValue"]/@content').extract_first(),
      'number_of_ratings': response.xpath('//meta[@itemprop="ratingCount"]/@content').extract_first(),
      'job_description': response.css('div#jobDescriptionText *::text').getall(),
    }
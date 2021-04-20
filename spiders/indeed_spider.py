import scrapy


class IndeedSpider(scrapy.Spider):
  name = 'indeed'

  start_urls = [
    'https://www.indeed.com/jobs?q=software+engineer&l=Remote&fromage=1'
  ]

  def parse(self, response):
    # for post in response.css("table#resultsBody"):
    full_descriptions = response.css('a.jobtitle')
    # yield from response.follow_all(full_descriptions, callback=self.parse_full_desc, cb_kwargs=dict(ad_url='hello',))
    for desc in full_descriptions:
      yield response.follow(desc, callback=self.parse_full_desc, cb_kwargs=dict(ad_url=desc.css('a::attr(href)').get(),))

    # for job_post in response.css('div.result'):
    #   job_title = [word.strip() for word in job_post.css('a.jobtitle *::text').getall() if word != ' ']
    #   yield {
    #     'job_title': (' ').join(job_title).strip(),
    #   }

  def parse_full_desc(self, response, ad_url=None):
    yield {
      'ad_url': ad_url,
      'job_title': response.css('h1.jobsearch-JobInfoHeader-title::text').get(),
      'company_rating': response.xpath('//meta[@itemprop="ratingValue"]/@content').extract_first(),
      'number_of_ratings': response.xpath('//meta[@itemprop="ratingCount"]/@content').extract_first(),
      'job_description': response.css('div#jobDescriptionText *::text').getall(),
    }
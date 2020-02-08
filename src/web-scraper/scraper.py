import scrapy
class WebSpider(scrapy.Spider):
    name = "web_spider"
    start_urls = ['https://www.canada.ca/en/employment-social-development/services/funding.html']
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'funding-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
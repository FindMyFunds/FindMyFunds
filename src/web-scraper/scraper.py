import scrapy
from scrapy.spiders import SitemapSpider
class WebSpider(SitemapSpider):
    name = "web_spider"
    allowed_domains = ['www.canada.ca']
    sitemap_urls = ['https://www.canada.ca/en/services/youth.sitemap.xml']
    sitemap_rules = [
        ('/programs/', 'parse_page')
        ]
    def parse(self, response):
        self.logger.info('parsing %r' % response.url)
    def parse_page(self, response):
        f = open("crawled_pages.txt", "a")
        f.write(response.text)
        f.close()


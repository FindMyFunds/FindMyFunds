import scrapy
from scrapy.spiders import SitemapSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

class WebSpider(SitemapSpider):
    name = "web_spider"
    allowed_domains = ['www.canada.ca']
    start_urls = ['https://www.canada.ca/en/services/youth.sitemap.xml']
    sitemap_rules = [('/programs/', 'parse_page')]
    
    def parse_page(self, response):
        print(response.body)

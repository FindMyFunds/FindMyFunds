import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector
import re

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
        items = []
        item = {}
        item['url'] = response.url
        item['title'] = response.selector.xpath('//title/text()').get()
        description = response.css('.mwsgeneric-base-html').xpath('.//section//text()').getall()
        processed_description = self.preprocess_description(description)
        item['description'] = processed_description
        items.append(item)
        return items 
    def preprocess_description(self, description):
        preprocess_description = [desc.strip() for desc in description]
        stop_words_list = [ 'and', 'you', 'to', 'the', 'The', '', 'of'] # use nltk later
        clean_description = (' '.join([re.sub(r"[,.!?&$:]+",'', word) for word in preprocess_description if not word in stop_words_list])).lower()
        return clean_description
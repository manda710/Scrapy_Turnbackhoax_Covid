import scrapy
from scrapy.http import Request
from ..items import ScraperItem
import json

class NewsturnbackhoaxSpider(scrapy.Spider):
    name = 'newsturnbackhoax'
    allowed_domains = ['turnbackhoax.id']
    start_urls = ['http://turnbackhoax.id/']
    
    def start_requests(self):
        # Open the JSON file which contains article links
        with open('E:/Amanda/SKRIPSWEET/ScrapTurnBackHoax_withLink/scraper/coba.json') as json_file:
            data = json.load(json_file)
    
        for p in data:
            print('URL: ' + p['link'])
        
            request = Request(p['link'],callback=self.parse_article_page)
            yield request
    
    def parse_article_page(self,response):
        items = ScraperItem()
        items['link'] = response.request.url 
        items['judul'] = response.css('h1.entry-title::text').extract_first()
        items['tanggal'] = response.css('span.entry-meta-date a::text').extract_first()
        items['artikel'] = response.css('div.entry-content p::text').extract_first()
        items['kategori'] = response.css('span.entry-meta-categories a::text').extract_first()
            
        #items['judul'] = ''.join(items['judul'])
        #items['tanggal'] = ''.join(items['tanggal'])
        #items['artikel'] = ''.join(items['artikel'])
        #items['kategori'] = ''.join(items['kategori'])

        #items['artikel'] = items['artikel'].replace('\n','')
        
        yield items

    def parse(self, response):
        pass

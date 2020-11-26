import scrapy
from ..items import ScraperItem


class LinkturnbackhoaxSpider(scrapy.Spider):
    name = 'linkturnbackhoax'
    page_number = 2
    allowed_domains = ['turnbackhoax.id']
    start_urls = ['http://turnbackhoax.id/']

    def parse(self, response):
        items = ScraperItem()
        news = response.css('article')
        
        for text in news:
             link = text.css('a::attr(href)').extract_first()
             items['link'] = link
             
             yield items
        
        next_page = 'https://turnbackhoax.id/page/'+str(LinkturnbackhoaxSpider.page_number)+'/'
        if LinkturnbackhoaxSpider.page_number <= 2:
            LinkturnbackhoaxSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        

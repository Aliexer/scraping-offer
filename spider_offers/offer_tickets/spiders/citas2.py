import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CitasCrawler(CrawlSpider):
    name = 'citas2'
    custom_setttings = {
        'COLSESPIDER_PAGECOUNT' : 3
    }

    download_delay = 1

    strat_urls = [
        'https://quotes.toscrape.com/'
    ]

    rules = (

        Rule(
            LinkExtractor(
                allow=r'/page'
            ),follow=True, callback='parse'
        ),

    )
    print('hello world')
    def parse(self, response):

        print('\n\n')
        print('*'*40)
        print('CITAS')
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print(quotes)

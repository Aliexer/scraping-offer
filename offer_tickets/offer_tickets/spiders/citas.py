import scrapy

class QuotesSpider(scrapy.Spider):
    name = "citas"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'https://quotes.toscrape.com/page/3/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):

        print('\n\n')
        print('*'*40)
        print('CITAS')
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        #limite = 5
        #for quote in quotes[0:limite]:
            #print(quote)
        #quote = quotes.split(sep=",")
        #for quote in quotes:
        test = []
        #test.append(quotes)
        test.extend(quotes)
        print(test)   
        #print(type(quotes))
        #print('there are ', len(quotes))
            #todo = []
            #quotelist = quote.split(sep='\n')
            #todo.extend(quotelist)
            #print(quotelist)
            #if quote:
                #todo.extend(quotelist)
            #print(result)
        #print(todo)
   
        #print(lista)
        print('*'*40)
        

        
        


            
        
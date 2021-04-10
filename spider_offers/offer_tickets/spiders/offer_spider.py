import scrapy 


# response.xpath('//h1[@class="section-heading"]/text()').get() titulo 
# response.xpath('//div[@class="card-small"]//div[@class="card-small-left"]/h4/text()').get()origen
# response.xpath('//div[@class="card-small"]//div[@class="card-small-left"]/h3/text()').get()destino
# response.xpath('//div[@class="card-small"]//div[@class="card-small-right"]//span[@class="small"]/text()').get()por persona
# response.xpath('//div[@class="card-small"]//div[@class="card-small-right"]//span[@class="price-card"]/text()').getall()precio


class OfferSpider(scrapy.Spider):
	name = 'offers'
	start_urls = [
		'https://latam.tiquetesbaratos.com/?gclid=CjwKCAiAnvj9BRA4EiwAuUMDf64odxjTgSb560brKIwAOkxdV6x6rXIIXropMO4cnb8acVir0hIKJRoC8cMQAvD_BwE'
	]

	def parse(self, response):
		
		title = response.xpath('//h1[@class="section-heading"]/text()').get()
		
		origen = response.xpath('//div[@class="card-small"]//div[@class="card-small-left"]/h4/text()').getall()
		for origin in origen:
			print(origin)	
		destino = response.xpath('//div[@class="card-small"]//div[@class="card-small-left"]/h3/text()').getall()
		for destination in destino:
			print(destination)
		precio = response.xpath('//div[@class="card-small"]//div[@class="card-small-right"]//span[@class="price-card"]/text()').getall()
		for preci in precio:
			print(preci)
		yield {
			'titulo':title,
			'origen':origen,
			'destino':destino,
			'precio':precio
		}


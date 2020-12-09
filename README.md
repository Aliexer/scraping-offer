this a aplications for search offer in air tickets

the url is https://latam.tiquetesbaratos.com/?gclid=CjwKCAiAnvj9BRA4EiwAuUMDf64odxjTgSb560brKIwAOkxdV6x6rXIIXropMO4cnb8acVir0hIKJRoC8cMQAvD_BwE

Fisrt stage:
xpath expression  for find the information.

second stage:
save the information in a json file

third stage:
show the information on a table from a django server and template HTML


comand:
scrapy crawl offers -o ofeers.json
 # run the scraper and save the information on json file

python manage.py runserver

# run server django





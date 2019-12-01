import scrapy

class ShowMyIP(scrapy.Spider):
    name = 'showip'

    # get proxy name from settings
    #useProxy = 'LMTRES'

    start_urls = ['https://www.showmyipaddress.eu/']

    def parse(self, response):
        ip_address = response.css('div.text-center > div ::text').extract_first()
        yield {'--------- My ip is -------- ' : ip_address}


import scrapy

class WhatIsMyIp(scrapy.Spider):
    name = 'myip'

    # get proxy name from settings
    useProxy = 'LMTRES'
    start_urls = ['https://www.showmyipaddress.eu/']

    def parse(self, response):
        ip_address = response.css('div.text-center > div ::text').extract_first()
        yield {'--------- My ip is -------- ' : ip_address}


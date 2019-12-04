import scrapy

class WhatIsMyIp(scrapy.Spider):
    name = 'myip'

    # get proxy name from settings
    useProxy = 'LMTRES'

    start_urls = ['https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/',
            'https://www.whatismyip.com/']

    def parse(self, response):
        ip_address = response.xpath("//ul[contains(@class, 'list-group')]/li/text()").extract()
        yield {'--------- My ip is -------- ' : ip_address}


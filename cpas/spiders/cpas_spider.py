# -*- coding: utf-8 -*-
import scrapy

CPAS_URL = 'cpas.antenna.nl'
PROTOCOL = 'http://'


class CpasSpiderSpider(scrapy.Spider):
    name = 'cpas-spider'
    allowed_domains = [CPAS_URL]
    start_urls = ['http://cpas.antenna.nl/node/5589']

    def parse(self, response):
        yield {
            'title': response.css(".biblio-field-contents-title").extract_first(),
        }

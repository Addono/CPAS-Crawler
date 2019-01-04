# -*- coding: utf-8 -*-
import html2text as html2text
import scrapy

CPAS_URL = 'cpas.antenna.nl'
CPAS_PATH = '/node/'
PROTOCOL = 'http://'


class CpasSpiderSpider(scrapy.Spider):
    name = 'cpas-spider'
    allowed_domains = [CPAS_URL]

    converter = html2text.HTML2Text()
    converter.ignore_links = True
    converter.ignore_tables = True
    converter.ignore_emphasis = True
    converter.ignore_images = True

    def __init__(self, start=None, end=None, *args, **kwargs):
        super(CpasSpiderSpider, self).__init__(*args, **kwargs)

        if not start or not end:
            raise ValueError('Both "start" and "end" arguments are required, pass them as arguments, e.g. `scrapy '
                             'crawl cpas-spider -a start=5000 -a end=5005`')

        self.start_urls = [PROTOCOL + CPAS_URL + CPAS_PATH + str(i) for i in range(int(start), int(end))]

    def parse(self, response):
        data = {}
        for row in response.css("#biblio-node tr"):
            row_title = row.css("td:nth-child(1)::text").extract_first()
            data[row_title] = self.converter.handle(row.css("td:nth-child(2)").extract_first()).strip()

        if len(data) > 0:
            yield data

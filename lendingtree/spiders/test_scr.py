import pytest
from scrapy import Spider, Request
from scrapy.http import HtmlResponse
import requests

class TestSpider(Spider):
    '''Scrapy used to generate sample.html for test'''
    name = "test"

    url ="https://www.lendingtree.com/reviews/personal/fig-loans/119574447"
    

    def start_requests(self):
        yield Request(self.url, self.parse)

    def parse(self, response):
        for title in response.xpath('//p[@class="reviewTitle"]/text()'):
            yield {'title': title.get()}

# Test part
from betamax import Betamax
from betamax.fixtures.unittest import BetamaxTestCase


with Betamax.configure() as config:
    # where betamax will store cassettes (http responses):
    config.cassette_library_dir = 'cassettes'
    config.preserve_exact_body_bytes = True


@pytest.mark.vcr()
def test_parse(url, target):
    response = requests.get(url)
    scrapy_response = HtmlResponse(url, body=response.content)
    assert Spider().parse(scrapy_response) == target



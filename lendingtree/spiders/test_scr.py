from scrapy import Spider, Request
from scrapy.http import HtmlResponse

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


class TestExample(BetamaxTestCase):  # superclass provides self.session

    def test_parse(self):
        example = TestSpider()

        # http response is recorded in a betamax cassette:
        response = self.session.get(example.url)

        # forge a scrapy response to test
        scrapy_response = HtmlResponse(body=response.content, url=example.url)

        result = example.parse(scrapy_response)

        self.assertEqual({'image_href': u'image1.html'}, result.next())
        self.assertEqual({'image_href': u'image2.html'}, result.next())
        self.assertEqual({'image_href': u'image3.html'}, result.next())
        self.assertEqual({'image_href': u'image4.html'}, result.next())
        self.assertEqual({'image_href': u'image5.html'}, result.next())

        with self.assertRaises(StopIteration):
            result.next()
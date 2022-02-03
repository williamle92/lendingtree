# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys



class LendingSpiderSpider(scrapy.Spider):
    name= "lending_spider"
    closespider_itemcount=100
    start_urls = [ 
        'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183'
    ]

    def start_requests(self):
        # overwrite the start_requests and set them with a selenium request object
        yield SeleniumRequest(
            url=f"https://www.lendingtree.com/reviews/{self.cat}",
            wait_time=1,
            callback=self.parse
        )
    

    def parse(self, response):
        driver = response.meta['driver']
        # Look for the more review button and set it to a variable
        more_review = driver.find_element_by_xpath('//button[@class="moreReviewBtn"]')
        # Pressing ENTER on more reviews to reveal the next pagination
        more_review.send_keys(Keys.ENTER)

        # Select for all the reviews to be looped through
        reviews = response.xpath("//div[contains(@class, 'col-xs-12 mainReviews')]")

        for review in reviews:
            yield {
                "title": review.xpath(".//p[@class='reviewTitle']/text()").get(),
                "content": review.xpath('.//p[@class="reviewText"]/text()').get(),
                "author": review.xpath('normalize-space(.//div[@class="hideText"]/p[@class="consumerName"]/text())').get(),
                "star_rating": review.xpath('.//div[@class="numRec"]/text()').get(),
                "date_of_review": review.xpath('.//p[@class="consumerReviewDate"]/text()').get()  
            }
        # Return the next page URL and pass it into selenium request object to run parse with URL next page
        next_page = response.xpath(".//ul[@class='lenderNav pagination']/li[@class='page-item']/a[@aria-label='Next Page']/@href").get()
        # If next page exists, keep going
        if next_page:
            yield SeleniumRequest(url=next_page, wait_time=3, callback=self.parse)
        



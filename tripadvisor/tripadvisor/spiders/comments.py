import scrapy
from ..items import TripadvisorItem


class TripCommentsSpider(scrapy.Spider):
    name = 'trip_comments'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-or5-Parque_Barigui-Curitiba_State_of_Parana.html#REVIEWS']

    def parse(self, response):
        item = TripadvisorItem()
        squares = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        for square in squares:
            item["author_name"] = square.xpath(".//div[@class='_2fxQ4TOx']/span/a/text()").get()
            item["author_from"] = square.xpath(".//span[@class='default _3J15flPT small']/text()").get()
            item["comment_title"] = square.xpath(".//div[@class='glasR4aX']/a//span/text()").get()
            item["comment_body"] = square.xpath(".//q[@class='IRsGHoPm']/span/text()").get()
            item["comment_date"] = square.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item

        # next_page = response.xpath("//a[@class='ui_button nav next primary ' and text()='Próximas']/@href").get()
        # if next_page:
        #     print(next_page)
        #     yield response.follow(url=next_page, callback=self.parse)

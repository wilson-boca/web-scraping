import scrapy


class TripadvisorItem(scrapy.Item):
    author_name = scrapy.Field()
    author_from = scrapy.Field()
    comment_title = scrapy.Field()
    comment_body = scrapy.Field()
    comment_date = scrapy.Field()

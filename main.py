import os

from tripadvisor.tripadvisor.spiders.comments import TripCommentsSpider
from scrapy.crawler import CrawlerProcess


if __name__ == "__main__":
    if os.path.exists('result.csv'):
        os.remove('result.csv')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_FIELDS': ["author_name", "author_from", "comment_title", "comment_body", "comment_date"],
        'FEED_URI': 'result.csv'
    })
    process.crawl(TripCommentsSpider)
    process.start()

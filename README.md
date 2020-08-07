# Python WebScraping

A Python web scraping project

### Installing

Installing requirements
```
$ mkvirtualenv web-scraping --python=python3
$ workon web-scraping
$ pip3 install -r requirements.txt
```

Running the crawler
```
To export to JSON
$ scrapy crawl trip_comments -o all_pages.json

To export to CSV
$ scrapy crawl trip_comments -o all_pages.csv
```

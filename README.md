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
Running the WordCloud generator
```
To craw and create imnage run the script
$ python main.py

To create the WordCloud image only:
$ python word_cloud.py
```
It will give you an image similar to this:

![WordCloud Trip](tripadvisor_word_cloud.png)
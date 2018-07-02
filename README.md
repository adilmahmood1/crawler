# crawler
A crawler built with scrapy in python (3.6) that crawls a given domain, extracting the title, url and http code of each page crawled.

1. Install scrapy.

> pip install scrapy

2. Clone the repository.

3. Run the following command to crawl the site (in this case 'https://caseblocks.com'):

> scrapy crawl spider1

4. To export as csv, run the following command:

> scrapy crawl spider1 -o data.csv

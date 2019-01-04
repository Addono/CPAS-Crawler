# CPAS Crawler
A Scrapy crawler to crawl the [CPAS Antenna database](http://cpas.antenna.nl/databases).

## Usage
### Local
Install the project locally:
```
git clone https://github.com/Addono/CPAS-Crawler
cd CPAS-Crawler
pip install -r requirements.txt
```

Run the crawler:
```
scrapy crawl cpas-spider -o output.json -a start=1508 -a end=13000
```

### Scrapinghub
1. Create a new project
1. Clone this repository as the source code of the project
1. Run the `cpas-spider`, make sure to set the arguments `start` and `end` to indiciate the ID of the first and last crawled element.

## Troubleshooting
Windows users might need to install the following packages `pypiwin32` and `pywin32`.

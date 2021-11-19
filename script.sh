#!/bin/sh

python3 /Users/HarrySmith/Dev/AmazonScraper/scraper.py > amazon.html

grep -E -i -o '[0-9]*\.[0-9]+' amazon.html  >> prices.csv

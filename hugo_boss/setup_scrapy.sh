#!/bin/bash

python -m scrapy startproject hugo_boss
cd project_name || exit
scrapy genspider hugo_prod https://www.hugoboss/home

python -m scrapy shell

python -m scrapy crawl hugo_prod
python -m scrapy crawl hugo_prod -o hugo_prod.csv
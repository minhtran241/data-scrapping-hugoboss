# Data Scrapping using Scrapy

Find more information about `Scrapy` in [Scrapy Documentation](https://scrapy-gallaecio.readthedocs.io/en/latest/index.html)

CMDs for generating `Scrapy` project are in `hugo_boss/setup_scrapy.sh` file

Scrape information of all products from [Hugo Boss's website](https://www.hugoboss.com/home)

## Data

-   Product's name
-   Available colors
-   Image URLs
-   Product's detail
-   Product's materials
-   Product's care information

## Scrapping Process

-   The scrapping process is in `hugo_boss/spiders/hugo_prod.py` file
-   Scrape information in parallel (32 maximum concurrent requests performed)
-   The data will be extracted and recorded in `hugo_boss/hugo_prod.csv` file

## Scrapy's report

```sh
 'downloader/request_bytes': 12888534,
 'downloader/request_count': 9135,
 'downloader/request_method_count/GET': 9135,
 'downloader/response_bytes': 420956479,
 'downloader/response_count': 9135,
 'downloader/response_status_count/200': 9086,
 'downloader/response_status_count/301': 7,
 'downloader/response_status_count/410': 42,
 'dupefilter/filtered': 21442,
 'elapsed_time_seconds': 3356.142286,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2022, 10, 22, 21, 47, 30, 840535),
 'httpcompression/response_bytes': 3399131472,
 'httpcompression/response_count': 9086,
 'httperror/response_ignored_count': 42,
 'httperror/response_ignored_status_count/410': 42,
 'item_scraped_count': 7951,
 'log_count/DEBUG': 17094,
 'log_count/ERROR': 319,
 'log_count/INFO': 108,
 'memusage/max': 281391104,
 'memusage/startup': 55468032,
 'request_depth_max': 116,
 'response_received_count': 9128,
 'scheduler/dequeued': 9135,
 'scheduler/dequeued/memory': 9135,
 'scheduler/enqueued': 9135,
 'scheduler/enqueued/memory': 9135,
 'spider_exceptions/AttributeError': 319,
 'start_time': datetime.datetime(2022, 10, 22, 20, 51, 34, 698249)
```

## Contributor

-   Minh Tran (Me)

# Lab 7: Using the Elastic Stack to study scraped data from a web page

In this lab we used [Scrapy](https://scrapy.org/) to collect data from The New York Times and IMDb website, and uploaded it into [Elasticsearch](https://www.elastic.co/elasticsearch/) to conduct analysis using [Kibana](https://www.elastic.co/kibana/). We analyzed actors that played a role in 80's films and their longevity. In the end, we presented a dashboard with visualizations that helped us in the analysis process.

## Group Information
* Candela Caceres, Julio Christians (julio.christians.candela@est.fib.upc.edu)
* Maatouk, Karim (fabricio.ferreira.da.silva@est.fib.upc.edu)

## Task 7.1: Extract selected information from a newspaper webpage

To execute this task we also had to install unidecode:

```sh
pip install unidecode
```

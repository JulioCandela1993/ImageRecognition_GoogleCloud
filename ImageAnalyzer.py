# -*- coding: utf-8 -*-
import scrapy
import googleapiclient.discovery
import requests
import base64

class ImageanalyzerSpider(scrapy.Spider):
    name = 'ImageAnalyzer'
    allowed_domains = ['gettyimages.es']
    start_urls = ['https://www.gettyimages.es/fotos/peru?mediatype=photography&phrase=peru&sort=mostpopular']

    service = googleapiclient.discovery.build('vision', 'v1')
    i=0
    def parse(self, response):
        for matrix_images in response.css(".search-content__gallery-assets"):
            for img_div in matrix_images.css('article'):
                url = img_div.css('img::attr(src)').extract_first()
                img_b64 = base64.b64encode(requests.get(url).content)
                service_request = self.service.images().annotate(body={
                    'requests': [{
                        'image': {
                            'content': img_b64.decode('UTF-8')
                        },
                        'features': [{
                            'type': 'LABEL_DETECTION',
                            'maxResults': 5
                        }]
                    }]
                })
    
                analytics_result = service_request.execute()
                print("Results for image %s:" % url)
                tags = {}
                for result in analytics_result['responses'][0]['labelAnnotations']:
                    tags.update({result['description']:result['score']})
                    print("%s - %.3f" % (result['description'], result['score']))
                yield {
                    'url': url,
                    'tags':tags
                }
                self.i=self.i+1
                if self.i >=100:
                    break
            if self.i >=100:
                break
            print('Here')
            next_page = response.css('.search-pagination__button--next::attr("href")').extract_first()
            print(next_page)
            yield response.follow(next_page, callback=self.parse)
        pass


p = {}
p.update({'tag':1})
#scrapy crawl ImageAnalyzer -o ImageAnalyzer.json
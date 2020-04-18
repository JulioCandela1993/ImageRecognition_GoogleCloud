import json
import os
import uuid

from elasticsearch import Elasticsearch
from pip._vendor import certifi

# Establish connection to Elastic Cloud
ELASTIC_API_URL = os.environ['ELASTIC_API_URL']
ELASTIC_API_USERNAME = os.environ['ELASTIC_API_USERNAME']
ELASTIC_API_PASSWORD = os.environ['ELASTIC_API_PASSWORD']

es = Elasticsearch([ELASTIC_API_URL],
                   http_auth=(ELASTIC_API_USERNAME, ELASTIC_API_PASSWORD),
                   ca_certs=certifi.where())

with open('ImageAnalyzer.json') as file:
    json = json.load(file)
    dict = []
    for item in json:
        for tag in item['tags']:
            es.index(index='cloudvision',
                     doc_type='tags',
                     id=uuid.uuid4(),
                     body={
                       'tag': tag,
                       'accuracy': item['tags'][tag]
                     })



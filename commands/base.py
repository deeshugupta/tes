from texttable import Texttable
from elasticsearch import Elasticsearch
import click

es =  Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])

def draw_table(response):
    table = Texttable(max_width=150)
    table.add_row(response[0].keys())
    for item in response:
        table.add_row(item.values())
    return table

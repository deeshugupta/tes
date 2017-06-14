from texttable import Texttable
from elasticsearch import Elasticsearch
import click
import json
import ConfigParser

filename = "/etc/tes/sources.ini"

es =  Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}])




def draw_table(response):
    table = Texttable(max_width=150)
    table.add_row(response[0].keys())
    for item in response:
        table.add_row(item.values())
    return table

def draw_single_response_table(response):
    table = Texttable(max_width=150)
    table.add_row(response.keys())
    table.add_row(response.values())
    return table


def pretty_print(response):
    parsed = json.loads(json.dumps(response))
    click.echo(json.dumps(parsed, indent=4, sort_keys=True))

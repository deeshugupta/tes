import base
import click

@click.group()
def node():
    '''
    Implementation of Cluster Nodes APIs of Elasticsearch
    '''
    pass

@node.command()
def info():
    try:
        response = base.es.nodes.info()
    except Exception as e:
        click.echo(e)
    else:
        base.pretty_print(response)

@node.command()
def stats():
    try:
        response = base.es.nodes.stats()
    except Exception as e:
        click.echo(e)
    else:
        base.pretty_print(response)

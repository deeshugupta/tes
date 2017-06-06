import base
import click

@click.group()
def cat():
    '''
    Implementation of Cat APIs of Elasticsearch
    '''
    pass


@cat.command('indices', short_help='The indices command provides a cross-section of each index.')
@click.option('--index', nargs=1, help=' A comma-separated list of index names to limit the returned information')
def indices(index):
    '''
    The indices command provides a cross-section of each index. This information spans nodes.
    We can tell quickly how many shards make up an index, the number of docs, deleted docs, primary store size, and total store size (all shards including replicas). All these exposed metrics come directly from Lucene APIs.
    '''
    try:
        response = base.es.cat.indices(index)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command('aliases', short_help='Information about current aliases')
@click.option('--name', nargs=1)
def aliases(name):
    '''aliases shows information about currently configured aliases to indices including filter and routing infos.'''
    try:
        response = base.es.cat.aliases(name)
        if not response:
            click.echo("No aliases as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('--node', nargs=1)
@click.option('--format', default='mb')
def allocation(node,format):
    try:
        response = base.es.cat.allocation(node_id=node,bytes=format)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('--index', nargs=1)
def count(index):
    try:
        response = base.es.cat.count(index)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command()
@click.option('--fields', nargs=1)
@click.option('--format', default='mb')
def fielddata(fields,format):
    try:
        response = base.es.cat.fielddata(fields=fields,bytes=format)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
def health():
    try:
        response = base.es.cat.health()
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

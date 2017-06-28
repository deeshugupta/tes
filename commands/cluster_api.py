import base
import click

@click.group()
def cluster():
    '''
    Implementation of Cluster APIs of Elasticsearch
    '''
    pass


@cluster.command()
@click.option('--level', nargs=1, help='''
specify level: cluster, indices(Default: cluster). Shards level is not supported as of now.
''')
def health(level):
    try:
        response = base.es.cluster.health(level=level)
        indices = None
        if(level == 'indices'):
            indices = response.pop('indices')
        table = base.draw_single_response_table(response)
        click.echo(table)
        if indices:
            for index in indices.keys():
                click.echo("Index is :"+index)
                click.echo(base.draw_single_response_table(indices[index]))
    except Exception as e:
        click.echo(e)


@cluster.command()
def state():
    try:
        response = base.es.cluster.state()
        # table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        base.pretty_print(response)

@cluster.command()
def stats():
    try:
        response = base.es.cluster.stats(human=True)
        # table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        base.pretty_print(response)

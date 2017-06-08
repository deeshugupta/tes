import base
import click

h_column_help = 'A comma-separated list of column names'
format_column_help = '''
The unit in which to display byte values, valid choices are: \'b\', \'k\', \'kb\', \'m\', \'mb\', \'g\', \'gb\', \'t\', \'tb\', \'p\', \'pb\'
'''
index_column_help = 'A comma-separated list of index names to limit the returned information'
@click.group()
def cat():
    '''
    Implementation of Cat APIs of Elasticsearch
    '''
    pass


@cat.command('indices', short_help='The indices command provides a cross-section of each index.')
@click.option('--index', nargs=1, help=index_column_help)
@click.option('-h', nargs=1, help=h_column_help)

def indices(index,h):
    '''
    The indices command provides a cross-section of each index. This information spans nodes.
    We can tell quickly how many shards make up an index, the number of docs, deleted docs, primary store size, and total store size (all shards including replicas). All these exposed metrics come directly from Lucene APIs.
    '''
    try:
        response = base.es.cat.indices(index, h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command('aliases', short_help='Information about current aliases')
@click.option('--name', nargs=1, help='A comma-separated list of alias names to return')
@click.option('-h', nargs=1, help=h_column_help)
def aliases(name,h):
    '''aliases shows information about currently configured aliases to indices including filter and routing infos.'''
    try:
        response = base.es.cat.aliases(name,h=h)
        if not response:
            click.echo("No aliases as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command('allocation', short_help='Information about shard allocation')
@click.option('--node', nargs=1, help='A comma-separated list of node IDs or names to limit the returned information')
@click.option('-h', nargs=1, help=h_column_help)
@click.option('--format', default='mb', help=format_column_help)
def allocation(node,format,h):
    '''
    Allocation provides a snapshot of how shards have located around the cluster and the state of disk usage
    '''
    try:
        response = base.es.cat.allocation(node_id=node,bytes=format, h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('--index', nargs=1)
@click.option('-h', nargs=1, help=h_column_help)
def count(index,h):
    try:
        response = base.es.cat.count(index,h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command()
@click.option('--fields', nargs=1)
@click.option('--format', default='mb')
@click.option('-h', nargs=1, help=h_column_help)
def fielddata(fields,format,h):
    try:
        response = base.es.cat.fielddata(fields=fields,bytes=format,h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def health(h):
    try:
        response = base.es.cat.health(h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def master(h):
    try:
        response = base.es.cat.master(h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def nodeattrs(h):
    try:
        response = base.es.cat.nodeattrs(h=h)
        if not response:
            click.echo("No attributes as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def nodes(h):
    try:
        response = base.es.cat.nodes(h=h)
        if not response:
            click.echo("No Nodes as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def pending_tasks(h):
    try:
        response = base.es.cat.pending_tasks(h=h)
        if not response:
            click.echo("No Pending Tasks as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def plugins(h):
    try:
        response = base.es.cat.plugins(h=h)
        if not response:
            click.echo("No Plugins as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())


@cat.command('recovery', short_help='recovery is a view of shard replication')
@click.option('--index', nargs=1, help=index_column_help)
@click.option('-h', nargs=1, help=h_column_help)
@click.option('--format', default='mb', help=format_column_help)
def recovery(index,format,h):
    try:
        response = base.es.cat.recovery(index=index,bytes=format, h=h)
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command()
@click.option('-h', nargs=1, help=h_column_help)
def repositories(h):
    try:
        response = base.es.cat.repositories(h=h)
        if not response:
            click.echo("No Repositories as of now")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command('segments', short_help='The segments command is the detailed view of Lucene segments per index.')
@click.option('--index', nargs=1, help=index_column_help)
@click.option('-h', nargs=1, help=h_column_help)
def segments(index,h):
    try:
        response = base.es.cat.segments(index=index, h=h)
        if not response:
            click.echo("No Segments present")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

@cat.command('shards', short_help='The shards command is the detailed view of what nodes contain which shards.')
@click.option('--index', nargs=1, help=index_column_help)
@click.option('-h', nargs=1, help=h_column_help)
def shards(index,h):
    try:
        response = base.es.cat.shards(index=index, h=h)
        if not response:
            click.echo("No Shards present")
            return
        table = base.draw_table(response)
    except Exception as e:
        click.echo(e)
    else:
        click.echo(table.draw())

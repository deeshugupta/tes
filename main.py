import click
import ConfigParser
import os

filename = "/etc/.tes/sources.ini"

@click.group()
def cli():
    pass
@cli.command('configure', short_help='Configure ES hosts')
@click.option('--name', prompt=True)
@click.option('--host', prompt=True)
@click.option('--port', prompt=True, type=int)
@click.option('--auth', prompt='Please provide basic authentiation(if any) in form of USER:PASSWORD', default='')
@click.option('--current', prompt='Do you want to make it your current ES config(y/N)')
def configure(name, host, port, auth, current):
    '''
    Configure is used to add various ES ports you are working on.
    The user can add as many es ports as the one wants,
    but one will remain active at one point.
    '''
    Config = ConfigParser.ConfigParser()
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except Exception as e:
            click.echo(e)
            return
    cfgfile = open(filename,'a')
    section_name = None
    if(current.lower() == 'y'):
        section_name = 'Current'
    else:
        section_name = name.capitalize()
    Config.add_section(section_name)
    Config.set(section_name,'host',host)
    Config.set(section_name,'port',port)
    Config.set(section_name,'auth',auth)
    Config.set(section_name,'name',name.capitalize())
    Config.write(cfgfile)
    cfgfile.close()

@cli.command('list', short_help='List the names of all the configurations.')
def list():
    Config = ConfigParser.ConfigParser()
    try:
        Config.read(filename)
    except Exception as e:
        click.echo(e)
        return
    sections = Config.sections()
    for section in sections:
        name = Config.get(section, 'name')
        if section == "Current":
            name = name + "*"
        click.echo(name)
    click.echo("* is name of the current configuration")


@cli.command('show', short_help='Shows the ES configuration')
@click.option("--name", help='''Name of the ES host.
If not provided it will show Current by Default''')
def show(name):
    Config = ConfigParser.ConfigParser()
    try:
        Config.read(filename)
    except Exception as e:
        click.echo(e)
        return
    if not name:
        name = 'Current'
    else:
        name = name.capitalize()
    options = Config.options(name)
    for option in options:
        click.echo('%s : %s' % (option.capitalize(), Config.get(name, option)))

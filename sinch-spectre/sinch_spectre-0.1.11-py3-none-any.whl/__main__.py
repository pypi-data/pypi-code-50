import click
from spectre import config

@click.group()
@click.option('--spectre-dir', default=None, help='Path to the spectre root directory (location of spectre config and target dir for generated files)')
@click.option('--debug', is_flag=True, default=False, help='Run in debug mode. Different effects depending on command')
def cli(spectre_dir, debug):
    global CONFIG
    CONFIG = config.load(spectre_dir)
    CONFIG.debug = debug
    pass

@click.group(help='Generate code based on an entity specification file')
def generate():
    pass

@click.group(name='import')
def handle_import():
    pass

@click.group()
def create():
    pass

@click.command(name='entity')
def create_entity():
    from spectre import creator
    creator.write_entity(CONFIG)

@click.command(name='mysql')
@click.argument('path')
def import_mysql(path):
    from spectre.importers import mysql
    written = mysql.import_mysql(CONFIG, path)
    click.echo(written)

@click.command()
@click.argument('path')
def proto(path):
    from spectre.generation import proto
    proto.generate(CONFIG, path)


@click.command()
@click.argument('path')
@click.option('--pojo', is_flag=True, help='Generate the base model java class corresponding to the entity')
@click.option('--spring-data', is_flag=True, help='Generate Spring Data artifacts, like Repository and Entity annotations. This will automatically set POJO generation')
@click.option('--spring-web', is_flag=True, help='Generate Spring Web REST controllers for CRUD')
@click.option('--manager', is_flag=True, help='Generate a CRUD Manager class wrapping the Spring Data repository')
@click.option('--dto', is_flag=True, help='Generate a DTO object corresponding to the entity itself')
@click.option('--all', '-a', 'generate_all', is_flag=True, help='Generate all the above')
def java(path, pojo, spring_data, spring_web, manager, dto, generate_all):
    from spectre.generation import java
    generator_options = {
        'pojo': pojo,
        'spring_data': spring_data,
        'spring_web': spring_web,
        'manager': manager,
        'dto': dto,
    }
    if generate_all:
        for key in generator_options.keys():
            generator_options[key] = True
    elif 'spring_data':
        generator_options['pojo']: True
    CONFIG.generator_options = generator_options
    click.echo(f'Generating java code from {path}')
    written = java.generate(CONFIG, path)
    for path in written:
        click.echo(path)

@click.command()
@click.argument('path')
def jhipster(path):
    from spectre.generation import jhipster
    click.echo(f'Generating jhipster entities from {path}')
    written = jhipster.generate(CONFIG, path)
    for path in written:
        click.echo(path)

cli.add_command(handle_import)
cli.add_command(generate)
cli.add_command(create)
handle_import.add_command(import_mysql)
create.add_command(create_entity)
generate.add_command(java)
generate.add_command(jhipster)
generate.add_command(proto)
cli()

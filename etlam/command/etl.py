import click
from etlam import processing


@click.command()
@click.argument('folder')
def run_etl(folder):
    click.echo('Run ETL process...')
    processing.run_etl(folder)
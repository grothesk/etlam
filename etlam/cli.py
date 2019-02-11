import click

from etlam.command import etl


@click.group()
def main():
    pass


main.add_command(etl.run_etl)
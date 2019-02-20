import click
from passwords import commands as passwords_commands

PASSVALUE_TABLE = '.passvalue.csv'
@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['passValue_table'] = PASSVALUE_TABLE

cli.add_command(passwords_commands.all)
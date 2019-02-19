import click
from passwords import commands as passwords_commands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command(passwords_commands.all)
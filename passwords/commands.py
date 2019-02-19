import click

@click.group()
def passwords():
    """Gestiona el ciclo de vida de las passwords/valores"""
    pass


@passwords.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Crea un nuevo set Value/Password """
    pass


@passwords.command()
@click.pass_context
def list(ctx):
    """Lista todos los valores almacenados"""
    pass


@passwords.command()
@click.pass_context
def update(ctx, password_to_update):
    """Actualiza un value/password"""
    pass


@passwords.command()
@click.pass_context
def delete(ctx, value_to_delete):
    """Elimina un pass/value"""
    pass


all = passwords

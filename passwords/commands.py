import click
from passwords.services import PassValueService
from passwords.models import PassValueModel


@click.group()
def passwords():
    """Gestiona el ciclo de vida de las passwords/valores"""
    pass


@passwords.command()
@click.option('-a', '--application',
        type=str,
        prompt=True,
        help="Qué aplicación/sistema/bd/servicio es? ")
@click.option('-n', '--value',
        type=str,
        prompt=True,
        help="Usuario/Login ")
@click.option('-p', '--password',
        type=str,
        prompt=True,
        help="Password ")
@click.option('-d', '--description',
        type=str,
        prompt=True,
        help="Una descripción del conjunto ")
@click.pass_context
def create(ctx, application, value, password, description):
    """Crea un nuevo set Value/Password """
    passValue = PassValueModel(application, value,password,description)
    passvalue_service = PassValueService(ctx.obj['passValue_table'])
    passvalue_service.create_passValue(passValue)

@passwords.command()
@click.pass_context
def list(ctx):
    """Lista todos los valores almacenados"""
    passvalue_service = PassValueService(ctx.obj['passValue_table'])
    passvalues = passvalue_service.list_passValues()
    click.echo('                 ID                 |   APP   |   VALUE   |   PASS   |   DESCRIPTION   ')
    click.echo('*'*100)
    for passvalue in passvalues:
            print('{pid}|   {app}   |   {value}   |   {password}   |   {description}   '.format(
                    pid = passvalue['pid'],
                    app = passvalue['application'],
                    value = passvalue['value'],
                    password = passvalue['password'],
                    description = passvalue['description']
            ))


@passwords.command()
@click.argument('passvalue_pid',
        type=str)
@click.pass_context
def update(ctx, passvalue_pid):
    """Actualiza un value/password"""
    passvalue_service = PassValueService(ctx.obj['passValue_table'])
    passvalues_list = passvalue_service.list_passValues()

    passvalue = [passvalue for passvalue in passvalues_list if passvalue['pid'] == passvalue_pid]

    if passvalue:
        pass
    else:
        pass


@passwords.command()
@click.pass_context
def delete(ctx, value_to_delete):
    """Elimina un pass/value"""
    pass


all = passwords

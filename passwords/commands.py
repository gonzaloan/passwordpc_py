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
    pass_value = PassValueModel(application, value,password,description)
    pass_value_service = PassValueService(ctx.obj['pass_value_table'])
    pass_value_service.create_pass_value(pass_value)

@passwords.command()
@click.pass_context
def list(ctx):
    """Lista todos los valores almacenados"""
    pass_value_service = PassValueService(ctx.obj['pass_value_table'])
    pass_values_list = pass_value_service.list_pass_values()
    click.echo('                 ID                 |   APP   |   VALUE   |   PASS   |   DESCRIPTION   ')
    click.echo('*'*100)
    for pass_value in pass_values_list:
            print('{pid}|   {app}   |   {value}   |   {password}   |   {description}   '.format(
                    pid = pass_value['pid'],
                    app = pass_value['application'],
                    value = pass_value['value'],
                    password = pass_value['password'],
                    description = pass_value['description']
            ))


@passwords.command()
@click.argument('pass_value_pid',
        type=str)
@click.pass_context
def update(ctx, pass_value_pid):
    """Actualiza un value/password"""
    pass_value_service = PassValueService(ctx.obj['pass_value_table'])
    pass_values_list = pass_value_service.list_pass_values()
    pass_value = [pass_value for pass_value in pass_values_list if pass_value['pid'] == pass_value_pid]
    if pass_value:
        pass_value = _update_pass_value_flow(PassValueModel(**pass_value[0]))
        pass_value_service.update_pass_value(pass_value)
        click.echo("Pass/Value actualizados")
    else:
         click.echo("Pass/Value no encontrados")

def _update_pass_value_flow(pass_value):
    click.echo("Dejar vacío si no se quiere modificar el valor")
    pass_value.value = click.prompt('Nuevo Value: ', type=str, default=pass_value.value)
    pass_value.password = click.prompt('Nueva Pass: ', type=str, default=pass_value.password)
    pass_value.description = click.prompt('Nueva Descripción: ', type=str, default=pass_value.description)
    return pass_value

@passwords.command()
@click.argument('pass_value_pid', type = str)
@click.pass_context
def delete(ctx, pass_value_pid):
    """Elimina un pass/value"""
    pass_value_service = PassValueService(ctx.obj['pass_value_table'])
    pass_values_list = pass_value_service.list_pass_values()
    pass_value = [pass_value for pass_value in pass_values_list if pass_value['pid'] == pass_value_pid]
    if pass_value:
        pass_value_service.delete_pass_value(pass_value)
        click.echo('Pass/Value borrado.')
    else:
        click.echo('Pass/Value no encontrado.')


all = passwords

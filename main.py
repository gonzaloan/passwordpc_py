import sys, csv, os

PASS_TABLE = '.pass.csv'
PASS_SCHEMA = ['application_name', 'password', 'description']
passwords_lists = []

def _initialize_passwords_from_storage():
    #Inicializamos la base de datos de solo lectura y leemos todo lo que contiene le archivo de bd

    with open(PASS_TABLE, mode = 'r') as f:
        reader = csv.DictReader(f, fieldnames=PASS_SCHEMA)
        for row in reader:
            passwords_lists.append(row)

def _save_passwords_to_storage():
    tmp_table_pass = '{}.tmp'.format(PASS_TABLE)
    with open(tmp_table_pass, mode = 'w') as f:
        writer = csv.DictWriter(f, fieldnames=PASS_SCHEMA)
        writer.writerows(passwords_lists)
        #Borramos la tabla primaria
        os.remove(PASS_TABLE)
        #Y modificamos el nombre de la temporal
    os.rename(tmp_table_pass, PASS_TABLE)


def append_password(password_new):
    print("-----Agregar llave-------")
    global passwords_lists
    if password_new not in passwords_lists:
        passwords_lists.append(password_new)
    else:
        print('La pass ya existe en la base de datos.')


def list_passwords():
    print("-----Listas valores-------")
    for idx, value in enumerate(passwords_lists):
        print('{id} | {value}'.format(id=idx, value=value))
    print("--------------------------")

def update_value(key_to_modify, updated_value):
    print("-----Actualizar valor-------")
    global passwords_lists
    if key_to_modify in passwords_lists:
        index = passwords_lists.index(key_to_modify)
        passwords_lists[index] = updated_value
    else:
        print("No existe el valor {}".format(key_to_modify))

def list_password_list():
    print(passwords_lists)

def delete_key_value(key_to_delete):
    global passwords_lists
    if(key_to_delete in passwords_lists):
        passwords_lists.remove(key_to_delete)
    else:
        print("No existe el valor {}".format(key_to_delete))

def search_value_pass(key_searched):
    for value in passwords_lists:
        if(value['application_name']!=key_searched):
            continue
        else:
            return True

def _print_welcome():
    print("Bienvenido a Tus Claves")
    print("*"*50)
    print("Que necesitas hacer?:")
    print("1- Agregar llaves")
    print("2- Listar valores ya almacenados")
    print("3- Actualizar valor de una llave ya creada")
    print("4- Eliminar llave y valor")
    print("5- Obtener una clave")
    print("X- Salir")

def _get_value_field(field_name):
    field = None
    while not field:
        field = input('Cuál es el valor {}?'.format(field_name))
    return field

def _get_value_name():
    return input("Cuál es el nombre de la llave?")


if __name__ == '__main__':
    _initialize_passwords_from_storage()

    while True:
        _print_welcome()
        command = input("Ingrese la opción: ")
        if command == '1':
            password_field = {
                'application_name' : _get_value_field('nombre aplicación'),
                'password' : _get_value_field('password'),
                'description': _get_value_field('descripción')
            }
            append_password(password_field)
        elif command == '2':
            list_passwords()
        elif command == '3':
            value_name = _get_value_name()
            updated_value = input('Cuál es el nuevo nombre del valor?')
            update_value(value_name, updated_value)

        elif command == '4':
            value_name = _get_value_name()
            delete_key_value(value_name)
        elif command == '5':
            value_name = _get_value_field('Valor')
            found = search_value_pass(value_name)
            if(found):
                print(passwords_lists[value_name])
            else:
                print("No existe el valor buscado")

        elif command.upper() == 'X':
            print("---------SALIR---------")
            break

    _save_passwords_to_storage()
    
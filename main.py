import sys

passwords_lists = {
    "pc": "Abril2019"
}

def append_password():
    print("-----Agregar llave-------")
    key = _get_key_from_user()
    value = _get_value_from_user()
    if key in passwords_lists:
        print("Ya existe este valor. ")
    else:
        passwords_lists[key] = value
        print("----Guardado OK----")


def list_passwords():
    print("-----Listas valores-------")
    for valor in passwords_lists:
        print(valor)
    print("--------------------------")

def update_value():
    print("-----Actualizar valor-------")
    key_to_modify = _get_key_from_user()
    updated_value = _get_value_from_user()
    if key_to_modify in passwords_lists:
        passwords_lists[key_to_modify] = updated_value
    else:
        print("No existe el valor {}".format(key_to_modify))

def delete_key_value():
    key_to_delete = _get_key_from_user()
    if key_to_delete in passwords_lists:
        passwords_lists.pop(key_to_delete)
    else:
        print("No existe el valor {}".format(key_to_delete))

def _get_value():
    key_to_search= _get_key_from_user()
    if key_to_search in passwords_lists.items():
        print("*"*50)
        print (passwords_lists[key_to_search])
        print("*"*50)
    else:
        print("No existe el valor {}".format(key_to_search))

def _get_key_from_user():
    key_from_user = None
    while not key_from_user:
        key_from_user = input("Ingrese la llave: ")
    
    return key_from_user

def _get_value_from_user():
    value_from_user = None
    while not value_from_user:
        value_from_user = input("Ingrese el value: ")
    
    return value_from_user


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

if __name__ == '__main__':
    while True:
        _print_welcome()
        command = input("Ingrese la opción: ")
        if command == '1':
            append_password()
            list_passwords()
        elif command == '2':
            list_passwords()
        elif command == '3':
            update_value()
        elif command == '4':
            delete_key_value()
        elif command == '5':
            _get_value()
        elif command.upper() == 'X':
            print("---------SALIR---------")
            break
    
import sys

passwords_lists = {
    "pc": "Abril2019"
}

def append_password(key, value):
    if key in passwords_lists:
        print("Ya existe este valor.")
    else:
        passwords_lists[key] = value


def list_passwords():
    for valor in passwords_lists:
        print(valor)


def update_value(key_to_modify, updated_value):
    if key_to_modify in passwords_lists:
        passwords_lists[key_to_modify] = updated_value
    else:
        print("No existe el valor {}".format(key_to_modify))

def delete_key_value(key_to_delete):
    if key_to_delete in passwords_lists:
        passwords_lists.pop(key_to_delete)
    else:
        print("No existe el valor {}".format(key_to_delete))

def _get_value(key_to_search):
    if key_to_search in passwords_lists:
        print (passwords_lists[key_to_search])
    else:
        print("No existe el valor {}".format(key_to_search))

def _get_key_from_user():
    key_from_user = None
    while not key_from_user:
        key_from_user = input("Ingrese la llave:")
    
    return key_from_user


def _print_welcome():
    print("Bienvenido a Tus Claves")
    print("*"*50)
    print("Que necesitas hacer?:")
    print("1- Agregar llaves")
    print("2- Listar valores ya almacenados")
    print("3- Actualizar valor de una llave ya creada")
    print("4- Eliminar llave y valor")
    print("5- Obtener una clave")

if __name__ == '__main__':
    _print_welcome()
    #command = input("")
    #if command == 1:
    print(_get_key_from_user())
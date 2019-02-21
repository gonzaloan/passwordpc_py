
PASSWORD = '123456'

#Esto es un decorador
def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña? ')
        if (password == PASSWORD):
            return func()
        else:
            print("La contraseña no es correcta")
    return wrapper

@password_required
def needs_password():
    print("La contraseña es correcta")

def upper(func):
    #args son argumentos
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return result.upper()
    return wrapper

@upper
def say_my_name(name):
    return ("Hola, {}".format(name))


if __name__ == '__main__':
    print(say_my_name('Gonzalo'))
    needs_password()
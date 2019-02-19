class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hola, mi nombre es {} '.format(self.name))
    
if __name__ == '__main__':
    person = Person('Gonzalo', 28)
    print('Edad: {} '.format(person.
    age))
    person.say_hello()


def my_decorator(f):
    def wrapper(name):
        print(f"Iam decorating you {name}")
        f(name)
    return wrapper

@my_decorator
def my_func(name):
    print(f'Hello Iam {name}')
    return True


class Person:
    def __init__(self, name):
        self.name = name


class Gender(Person):
    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender

    def __repr__(self):
        return f'Iam {self.name}, gender: {self.gender}'


me = Gender(name='saf', gender='undefined')
print(me)
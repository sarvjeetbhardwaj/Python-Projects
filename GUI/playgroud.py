def add_nummbers(*args):
    sum=0
    for n in args:
        print(n)
        sum=sum+n

    return sum

def calculate(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
    return kwargs

class Car:

    def __init__(self, **kwargs):
        self.make=kwargs['make']
        self.engine=kwargs.get('engine')

    def print_model(self):
        print(f'Cars name is {self.make} & engine size is {self.engine}')

car=Car(make='Ford')
car.print_model()




# Animal is-a Object
class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):

    # Dog has-a __init__ that takes self and name as parameters
    def __init__(self, name):
        self.name = name


# Cat is-a Animal
class Cat(Animal):

    # Cat has-a __init__ that takes in self, name as params
    #
    def __init__(self, name):
        self.name = name

# Person is-a object
class Person(object):

    # Person has-a __init__ that takes in self, name as params.
    def __init__(self, name):
        self.name = name

        self.pet = None

# Employee is-a Person
class Employee(Person):

    # Employee has-a __init__ that takes in self, name and salary as params
    def __init__(self, name, salary):

        super(Employee, self).__init__(name)

        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass


rover = Dog('Rover')

satan = Cat('Satan')

mary = Person('Mary')

frank = Employee('Frank', 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

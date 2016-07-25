## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class
class Dog(Animal):

    def __init__(self, name):
        ## name is-a object
        self.name = name

## CAt is-a class
class Cat(Animal):

    def __init__(self, name):
        ## name is-a object
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## name is-a object
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## Super create employee object that inherites has-a
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a Object
class Fish(object):
    pass

## Salmon is-a Object
class Salmon(Fish):
    pass

## Halibut is-a object
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## sat is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a cat that is satn
mary.pet = satan

## Frank is-a Empolyee Frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet that pet has-a name rover
frank.pet = rover

## flipper is-a object
flipper = Fish()

## crouse is-a object
crouse = Salmon()

## harry is-a object
harry = Halibut()

class Mammal:
    def walk(self):
        print("walk")


class Cat(Mammal):
    pass
#pass basically told python to ignore empty class


class Dog(Mammal):
    def bark(self):
        print("bark!")


cat1 = Cat()
cat2 = Cat()

dog1 = Dog()
dog2 = Dog()

dog1.bark()
dog2.walk()
cat1.walk()
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, My name is {self.name}")

Robin = Person("Robin")
Robin.talk()
class Animal:
    
    def __init__(self, carnivore, herbivore):
        self.carnivore = carnivore
        self.herbivore = herbivore

    def eating (self, animal):
        print(f"{animal} is eating")
        
    def sleeping(self, animal):
        print(f"{animal} is sleeping")

class Dog(Animal):
    def __init__(self):
        super().__init__(carnivore=True, herbivore=False)

class Cat(Animal):
    def __init__(self):
        super().__init__(carnivore=False, herbivore=True)

dog = Dog()
dog.eating("Dog")
dog.sleeping("Dog")

cat = Cat()
cat.eating("Cat")
cat.sleeping("Cat")

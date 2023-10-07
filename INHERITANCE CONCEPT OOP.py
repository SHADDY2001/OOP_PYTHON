# Base class (parent class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # This method will be overridden in the derived classes

# Derived class 1 (child class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} the {self.species} says Woof!"

# Derived class 2 (child class)
class Cat(Animal):
    def speak(self):
        return f"{self.name} the {self.species} says Meow!"

# Create instances of the derived classes
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

# Call the speak method on instances
print(dog.speak())  # Output: Buddy the Dog says Woof!
print(cat.speak())  # Output: Whiskers the Cat says Meow!

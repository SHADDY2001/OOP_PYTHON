class Person:
    # Constructor to initialize the object with a name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating instances (objects) of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes and calling methods
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30
print(person1.greet())  # Output: Hello, my name is Alice and I am 25 years old.
print(person2.greet())  # Output: Hello, my name is Bob and I am 30 years old.

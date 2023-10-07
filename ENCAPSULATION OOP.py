class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self._age = age     # Protected attribute

    # Public method to get the name
    def get_name(self):
        return self.__name

    # Public method to set the age
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

    # Public method to display student information
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self._age}")

# Create a Student object
student1 = Student("Alice", 20)

# Accessing private and protected attributes through public methods
name = student1.get_name()
student1.set_age(21)
student1.display_info()

# Attempting to access private attribute directly (not recommended)
# This will raise an error
# print(student1.__name)

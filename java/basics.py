# Variables: Storing values in memory
name = "John"
age = 25

# Data Types: Different types of data
# Integer: Whole numbers
num = 10
# Float: Decimal numbers
pi = 3.14
# String: Textual data
message = "Hello, world!"
# Boolean: True or False values
is_true = True

# Arithmetic Operations: Basic mathematical operations
result = 5 + 3  # Addition
result = 10 - 4  # Subtraction
result = 6 * 2  # Multiplication
result = 8 / 4  # Division
result = 10 % 3  # Modulo (remainder)

# Conditional Statements: Executing code based on conditions
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops: Repeating code
# For loop: Iterating over a sequence of elements
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# While loop: Repeating code until a condition is met
count = 0
while count < 5:
    print(count)
    count += 1

# Functions: Reusable blocks of code
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# Lists: Ordered collection of elements
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

# Accessing list elements using index
print(numbers[0])  # Output: 1

# Dictionaries: Key-value pairs
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing dictionary values using keys
print(person["name"])  # Output: John

# Classes and Objects: Blueprint for creating objects
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started.")

my_car = Car("Toyota", "Camry")
print(my_car.make)  # Output: Toyota
my_car.start_engine()  # Output: Engine started.

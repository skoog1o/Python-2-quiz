# pythonquiz2.py

# VARIABLES
my_name = "Jeremiah"
print("My name is:", my_name)

# DATA TYPES
age = 22
greeting = "Hello!"
grades = [90, 85, 88]

print("age:", age, "->", type(age))
print("greeting:", greeting, "->", type(greeting))
print("grades:", grades, "->", type(grades))

# FUNCTIONS
def square_number(x):
    return x * x

print("The square of 25 is:", square_number(5))

# CLASSES
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def meow(self):
        return f"{self.name} the {self.color} cat says meow!"

my_cat = Cat("Moe", "Orange")
print(my_cat.name, my_cat.color)
print(my_cat.meow())

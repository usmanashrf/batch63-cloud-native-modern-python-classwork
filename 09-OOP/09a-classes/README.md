# Classes:
Imagine we’re trying to categorize everything in the world into two main groups:

Living Things: Things that are alive, like humans, animals, and plants.
Non-Living Things: Objects that do not have life, like cars, rocks, and furniture.

From there, we can further divide Living Things into:
- Humans
- Plants

And within Humans, we can even have specific types, like:
- Male
- Female

This is how we naturally organize things, and it’s very similar to how classes and objects work in programming.

---

## What are Classes in Python?

In Python, a class allows you to create a blueprint for something (like a HUMAN). From this blueprint, you can create objects, each with its own attributes and methods. Think of a class as a category and objects as the actual instances that belong to that category.

Key Terms:
Class: A blueprint or template for creating objects.
Object: An instance of a class. Each object has its own attributes and can perform actions.
Attributes: The data or properties related to an object (e.g., a name, height or age).
Methods: The actions or functions that an object can perform (e.g., a human can breathe, walk etc).


## How to write Class code

```
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking.")

# Create an instance (object) of the class
person = Human("Alice", 25)

# Call the speak method
person.speak()  # Output: Alice is speaking.

```

### Let’s break down the syntax of the Human class step by step:

def __init__(self, name, age, gender):
__init__ is a special method called a constructor. This method is automatically called when an object is created from the class.
It initializes the object's attributes (or properties) — name, age, and gender in this case.

**Parameters:**

self: Refers to the instance (or object) of the class. It allows the object to reference its own attributes and methods. Every method in a class must have self as the first parameter.
name, age, gender: These are the parameters passed to the constructor when creating an object of the Human class.

### self Must Be the First Parameter in Methods
In Python, every method in a class must include self as the first parameter. This is because the method needs to know which instance of the class it is working with. However, when you call the method, you don't need to pass self explicitly — Python automatically does this behind the scenes.



**def speak(self):**

This defines a method named speak that is part of the Human class. Methods are functions that belong to a class and define actions the objects of the class can perform.
The speak method allows the Human object to "speak" by printing a message.

**person = Human("Alice", 25, "Female")**

This creates an instance (or object) of the Human class.
Human("Alice", 25, "Female") calls the __init__ method, passing "Alice", 25, and "Female" as arguments. These values will be used to initialize the attributes of the person object.
After this line, the object person has the following attributes:

person.name = "Alice"
person.age = 25
person.gender = "Female"

---

**What Happens if You Use a Different Name for the Constructor other then __init__?**

```
class Human:
    def initialize(self, name, age):  # Using a non-standard method name
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

# Create an instance of the Human class
person = Human()  # No arguments passed, because no __init__ method is called automatically

# Call initialize method explicitly
person.initialize("Alice", 25)  # Now we must call this manually

# Call the speak method
person.speak()  # Output: My name is Alice, and I am 25 years old.

```

--- 
**What if You use any Different name as the first parameter in a Constructor other then self**

You can technically use any other name as the first parameter in a class method, and Python will still treat it as the instance of the object. However, it's highly recommended to stick to self for clarity and consistency.

```
class Human:
    def __init__(instance, name, age):  # Using 'instance' instead of 'self'
        instance.name = name
        instance.age = age

    def speak(instance):  # Using 'instance' instead of 'self'
        print(f"My name is {instance.name}, and I am {instance.age} years old.")
```

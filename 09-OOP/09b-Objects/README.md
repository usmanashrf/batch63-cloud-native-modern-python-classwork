## What Are Objects in Python?

In Python, an object is an instance of a class. While a class is like a blueprint or template, an object is the actual thing created from that blueprint. Objects have both attributes (data or properties) and methods (functions or actions they can perform) defined by the class.

### How to Create Objects

To create an object in Python, you simply call the class as if it were a function, passing the required arguments to its constructor (typically the __init__ method). The class then returns a new object (instance) of that class.

```
object_name = ClassName(arguments)

```


Example:
Let's say we have a class Human:

```
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# Create an object
person = Human("Alice", 25)

# Access the object's methods and attributes
person.speak()  # Output: My name is Alice and I am 25 years old.

```

In this example:

Human is the class.
person is an object (or instance) of the Human class.
"Alice" and 25 are passed as arguments to the __init__ constructor method, which sets the object's name and age attributes.



# Python OOP: Class Variables, Class Methods, and Static Methods

## 1. **Class Variables**

### What Are Class Variables?
- **Class variables** are variables that are shared among all instances of a class.
- They are defined within the class but outside any methods.
- All instances of the class have access to the same class variable.

### When to Use Class Variables?
- Use class variables when you want to store data that should be shared across all instances of the class. 
- Commonly used for **constants** or **counters** that track information related to all objects of the class.

### Example of Class Variables:

```python
class Car:
    # Class variable
    number_of_wheels = 4
    
    def __init__(self, model):
        # Instance variable
        self.model = model

# Accessing class variable
print(Car.number_of_wheels)  # Output: 4

# Creating instances
car1 = Car("Toyota")
car2 = Car("Honda")

# Both instances share the same class variable
print(car1.number_of_wheels)  # Output: 4
print(car2.number_of_wheels)  # Output: 4

# Modifying class variable through class
Car.number_of_wheels = 3
print(car1.number_of_wheels)  # Output: 3
```

### Key Points:
- Class variables are shared among all instances of a class.
- Changing a class variable affects all instances.

---

## 2. **Class Methods**

### What Are Class Methods?
- **Class methods** are methods that are bound to the class, not the instance.
- They can access and modify class variables.
- A class method is defined using the `@classmethod` decorator, and the first parameter is `cls` (the class itself).

### When to Use Class Methods?
- Use class methods when you need to modify class-level data (like class variables).
- Class methods are often used to create factory methods that instantiate objects in a certain way.

### Example of Class Methods:

```python
class Car:
    number_of_cars = 0  # Class variable
    
    def __init__(self, model):
        self.model = model
        Car.number_of_cars += 1  # Modify class variable in the constructor
    
    @classmethod
    def get_number_of_cars(cls):
        return f"Total cars: {cls.number_of_cars}"

# Creating instances
car1 = Car("Toyota")
car2 = Car("Honda")

# Using the class method to access class variable
print(Car.get_number_of_cars())  # Output: Total cars: 2
```

### Key Points:
- Class methods can modify class variables and are called on the class, not on instances.
- They are useful when you need to perform actions that affect the class itself rather than individual instances.

---

## 3. **Static Methods**

### What Are Static Methods?
- **Static methods** are methods that do not depend on class or instance data.
- They are defined using the `@staticmethod` decorator.
- Static methods do not have access to `cls` (class) or `self` (instance). They behave just like regular functions but are included within a class for logical grouping.

### When to Use Static Methods?
- Use static methods when you want a function that logically belongs to a class but does not need to access or modify class/instance-specific data.
- Good for utility functions that operate independently of class or instance data.

### Example of Static Methods:

```python
class MathOperations:
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b

# Using static methods without creating an instance
print(MathOperations.add(5, 3))        # Output: 8
print(MathOperations.subtract(10, 4))  # Output: 6
```

### Key Points:
- Static methods are independent of class and instance.
- They are typically used for utility or helper functions related to the class.

---

## Summary: When to Use Each Concept

| Concept        | When to Use                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------|
| **Class Variables**  | When you want to store data that is shared among all instances (e.g., counters, constants).          |
| **Class Methods**    | When you need to access or modify class-level data or want a method that logically affects the entire class. |
| **Static Methods**   | When you need a utility function that doesn’t require access to class or instance-specific data.      |

---

## Example: Using All Concepts Together

```python
class Car:
    number_of_cars = 0  # Class variable
    
    def __init__(self, model):
        self.model = model
        Car.number_of_cars += 1  # Increment class variable
    
    @classmethod
    def get_number_of_cars(cls):
        return f"Total cars: {cls.number_of_cars}"
    
    @staticmethod
    def car_type():
        return "Four-wheeled vehicle"

# Creating instances
car1 = Car("Toyota")
car2 = Car("Honda")

# Accessing class variable using class method
print(Car.get_number_of_cars())  # Output: Total cars: 2

# Using static method
print(Car.car_type())  # Output: Four-wheeled vehicle
```

### Breakdown:
- **Class Variable:** `number_of_cars` tracks the total number of car objects created.
- **Class Method:** `get_number_of_cars` allows us to access the class variable and get the total count of cars.
- **Static Method:** `car_type` is a utility method that returns a description of a car but does not interact with any instance or class-level data.



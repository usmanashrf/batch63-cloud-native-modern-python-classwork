# Composition in Python (OOP)

## 1. **What is Composition in Object-Oriented Programming (OOP)?**
- **Composition** is a concept in OOP where one class is composed of one or more objects from other classes. 
- It describes a **"has-a" relationship** between classes.
  - Example: A **Car** "has-an" **Engine**, or a **Library** "has-many" **Books**.

## 2. **Difference Between Inheritance and Composition**
- **Inheritance** represents an "is-a" relationship.
  - Example: A **Dog** "is-a" **Animal**.
- **Composition** represents a "has-a" relationship.
  - Example: A **Car** "has-an" **Engine**.

| Inheritance | Composition |
|-------------|-------------|
| "is-a" relationship | "has-a" relationship |
| Parent-child structure | Whole-part structure |
| A subclass inherits behavior from a parent class | A class contains objects of other classes to perform part of its functionality |

## 3. **Why Use Composition?**
- **Reusability:** Instead of repeating code, you can reuse components (classes) in different objects.
- **Separation of Concerns:** Each class is responsible for a single part of the functionality, making the code easier to maintain and test.
- **Flexible Code:** You can change the components (parts) without affecting the whole object. For example, you can switch engines in a car without changing the entire car design.

## 4. **Example: Composition in Python**

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower} horsepower starts.")

class Car:
    def __init__(self, model, horsepower):
        # Composition: Car "has-an" Engine
        self.model = model
        self.engine = Engine(horsepower)
    
    def drive(self):
        self.engine.start()  # Using the Engine to start the car
        print(f"{self.model} is now driving.")


my_car = Car("Toyota Camry", 268)
my_car.drive()
```

**Explanation:**
- The `Car` class is composed of an `Engine` object.
- The `Car` class doesn't inherit from `Engine`, but uses it to perform its functionality.
- This is a flexible and modular design. If you need to change the type of `Engine`, you only modify the `Engine` class without touching the `Car` class.

## 5. **When and Where to Use Composition**
- **Use Composition** when:
  1. You want to model a "has-a" relationship.
  2. You need **modular components**. For example, if you have a class for `Engine` in a car, you can reuse it in other classes like `Motorcycle` or `Truck`.
  3. You want to **separate concerns**. Each class can focus on one task (like `Engine` handles starting, while `Car` handles driving).
  4. You want to create more **flexible designs**. You can change the internal components without breaking the system (e.g., replacing the engine in a car).

- **Avoid Composition** if:
  1. You need to model a natural "is-a" relationship (like **Dog** and **Animal**). In such cases, use inheritance.
  2. The component class (`Engine`, in this case) isn’t truly a part of the whole object.

## 6. **Advantages of Composition**
- **Better Modularity**: Each part of the system (like the engine in a car) is encapsulated in its own class.
- **Easier Maintenance**: Smaller, specialized classes are easier to maintain, extend, and debug.
- **Loose Coupling**: Objects are loosely connected, making them more adaptable to changes. You can swap one part without affecting the whole system.

## 7. **Advanced Composition Concepts**
- **Multiple Compositions**: A class can be composed of more than one other class.
  - Example: A `Car` might have both `Engine` and `Wheel` objects.
  
```python
class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, model, horsepower, wheel_size):
        self.model = model
        self.engine = Engine(horsepower)  # Car has-an Engine
        self.wheels = Wheel(wheel_size)  # Car has four Wheels
    
    def drive(self):
        self.engine.start()
        print(f"{self.model} with {self.wheels}-inch wheels is now driving.")

my_car = Car("Ford Mustang", 450, 19)
my_car.drive()
```

In this case, the car "has-an" engine and "has wheels," showcasing how multiple compositions can work together in a class.


## 8. **Another way to use Composition**
```python
class FloorDivision():
    def division(self, dividend, divisor):
        print(f"Floor division {dividend // divisor}")
        
class SimpleDivision():
    def division(self, dividend, divisor):
        print(f"Simple Division {dividend / divisor}")

class Division():
    def __init__(self, division_decider):
        self.division_decider = division_decider
    
    def divide(self, dividend, divisor):
        self.division_decider.division(dividend, divisor)

# Create instances separately
a = FloorDivision()
b = SimpleDivision()

# Pass FloorDivison instance in Division Class
c = Division(a)
c.divide(11,4)

# Pass SimpleDivison instance in Division Class
d = Division(b)
d.divide(11,4)

# Create the instances of Division Class directly
floor_division = Division(FloorDivision())
simple_division = Division(SimpleDivision())

# Performing division operations
floor_division.divide(11, 5)
simple_division.divide(11, 5)
```
**Key Concepts:**
* Polymorphism: This example also demonstrates the concept of polymorphism, where the Division class can work with different types of division (floor or simple) depending on the object passed to it.

* Encapsulation: The division logic (either floor or simple) is encapsulated inside individual classes (FloorDivision and SimpleDivision). The Division class itself encapsulates the decision logic for which type of division to use.

* Abstraction: The Division class provides a simplified interface (divide()), hiding the complex logic of choosing between floor division and simple division. This way, the user only interacts with a simple, abstracted method without needing to know the internal details

# **Abstraction, Abstract Classes, and Abstract Methods in Python**

## **1. Introduction to Abstraction in Python OOP**

### **What is Abstraction?**
In Object-Oriented Programming (OOP), **abstraction** is the concept of **hiding the internal details** of an object and **exposing only the necessary information**. It allows you to work with higher-level concepts without getting bogged down by the details of how something works.

Think of a **car**:
- You know that you need to press the accelerator to move faster, but you don’t need to know how the engine works to achieve that. That’s abstraction — you only need to know what to do, not how it happens.

In Python, abstraction is typically achieved through **abstract classes** and **abstract methods**.

### **When to Use Abstraction?**
- When you need to define a common **interface** for multiple related objects (like defining how all types of shapes must have a method to calculate their area).
- When you want to **hide complexity** from users and provide them with a simplified way to interact with objects.
- When you want to **enforce** that certain methods should be implemented by all subclasses, but you don’t want to provide a specific implementation in the base class.

---

## **2. Abstract Classes in Python**

### **What is an Abstract Class?**
An **abstract class** in Python is a class that **cannot be instantiated** directly. It serves as a **blueprint** for other classes. Abstract classes may contain abstract methods that **must** be implemented by any subclass that inherits from the abstract class.

In Python, abstract classes are defined using the `abc` module (Abstract Base Classes).

### **Why Use Abstract Classes?**
- To **enforce a contract**: If you want to ensure that all subclasses implement certain methods, you can define those methods as abstract in the base class.
- To provide **partial implementation**: You can define common methods in the abstract class and leave specific details to the subclasses.

### **How to Create an Abstract Class?**
1. Import `ABC` (Abstract Base Class) from the `abc` module.
2. Inherit from `ABC` in your base class.
3. Use the `@abstractmethod` decorator to mark methods that must be implemented by subclasses.

---

## **3. Abstract Methods in Python**

### **What is an Abstract Method?**
An **abstract method** is a method that is **declared but contains no implementation**. Subclasses of an abstract class **must provide an implementation** for the abstract methods. Abstract methods are defined using the `@abstractmethod` decorator.

### **When to Use Abstract Methods?**
- When you want to **force subclasses** to implement a particular method.
- When you need to define methods in the base class that have **no meaningful default behavior**, and it’s up to the subclasses to define them.

---

## **4. Example of Abstraction, Abstract Classes, and Abstract Methods**

Here’s a simple example that shows how to use abstraction, abstract classes, and abstract methods in Python.

### **Example: Shape Class with Different Types of Shapes**

```python
from abc import ABC, abstractmethod

# Abstract class representing the concept of a shape
class Shape(ABC):
    
    # Abstract method to calculate area
    @abstractmethod
    def area(self):
        pass
    
    # Abstract method to calculate perimeter
    @abstractmethod
    def perimeter(self):
        pass
    
    # Common method in the abstract class
    def description(self):
        return "This is a shape object"

# Subclass for a Rectangle
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # Implementing the abstract method 'area'
    def area(self):
        return self.length * self.width
    
    # Implementing the abstract method 'perimeter'
    def perimeter(self):
        return 2 * (self.length + self.width)

# Subclass for a Circle
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    # Implementing the abstract method 'area'
    def area(self):
        return 3.1416 * self.radius * self.radius
    
    # Implementing the abstract method 'perimeter'
    def perimeter(self):
        return 2 * 3.1416 * self.radius

# Instantiate the subclasses
rect = Rectangle(5, 3)
circle = Circle(4)

# Access the abstract methods
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

# Access the common method from the abstract class
print(rect.description())
print(circle.description())
```

### **Explanation of the Example:**
1. **Shape Class**: 
   - This is an abstract class because it inherits from `ABC`.
   - It contains two abstract methods: `area()` and `perimeter()`, which **must** be implemented by any subclass.
   
2. **Rectangle and Circle**:
   - These are concrete classes that **inherit** from `Shape`.
   - They **implement** the abstract methods `area()` and `perimeter()`.
   - These subclasses provide specific implementations for calculating the area and perimeter of rectangles and circles.
   
3. **Common Behavior**: 
   - Both `Rectangle` and `Circle` inherit the `description()` method from the `Shape` class, which is **not abstract**, and therefore provides a common behavior for all shapes.

### **Key Points:**
- You **cannot instantiate** the `Shape` class directly (e.g., `Shape()` would raise an error).
- The subclasses **must** implement all the abstract methods from the `Shape` class, or they will also be abstract.
- **Abstraction** here is the concept of working with "shapes" without needing to know the specifics of whether it’s a rectangle or circle, as both implement the methods required by the abstract class.

---

## **5. Real-World Use Cases of Abstraction**

- **Frameworks**: Abstract classes are often used in frameworks where base functionality is defined, and the users of the framework must implement specific details. For example, GUI frameworks may have an abstract class `Window` with abstract methods like `draw()`, which concrete window classes must implement.
  
- **Game Development**: You might have an abstract class `GameCharacter` that defines abstract methods like `attack()`, `defend()`, and `move()`. Each specific character (e.g., `Warrior`, `Mage`, `Archer`) must implement these methods differently.

---

## **6. Key Takeaways**

- **Abstraction** is about **hiding complexity** and exposing only what’s necessary.
- **Abstract classes** serve as blueprints for creating concrete subclasses. They cannot be instantiated directly.
- **Abstract methods** are declared in abstract classes but must be implemented by any subclass.
- Abstraction and abstract classes allow for the creation of a **flexible and scalable code structure** where specific details are handled by subclasses.

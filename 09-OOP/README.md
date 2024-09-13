## Understanding Procedural Programming and Object-Oriented Programming (OOP)

When you start learning to code, you’ve likely started with Procedural Programming write programs using functions, loops, and put everything (data, logic, functions) in a single file or in just a few files without much structure, we often refer to it as a spaghetti code or Procedural programming  (if it's messy and hard to follow).

### What is Procedural Programming?

Procedural programming is the approach most beginners take when they first learn to code. It focuses on writing step-by-step instructions for the computer to follow. In this style, your program is essentially a series of commands and functions that perform actions on data.

**Key Features of Procedural Programming:**

- Functions: The main building blocks are functions. Each function performs a specific task, like adding two numbers, printing a message, or looping through data.
- Sequential Execution: The program runs in a top-down manner, following the order of functions and instructions.
- Data and Functions Are Separate: Data (like variables) and the functions that act on that data are kept separate. This means you define variables first and then create functions that manipulate these variables.


### Issues with Procedural Programming:
- Hard to Manage Large Programs: As your program grows, keeping track of all the functions and variables becomes difficult. You might end up with many functions doing similar things, leading to confusion.

- Code Duplication: If you need the same functionality for different parts of your program, you often end up copying and pasting code, which makes it hard to maintain.

- No Data Encapsulation: In procedural programming, data is accessible from anywhere, making it easier to accidentally modify variables, leading to bugs.

- Poor Scalability: When you want to add new features, you need to modify the existing functions and variables, which can lead to breaking other parts of the program.

---

## Object-Oriented Programming (OOP) 

As programs become more complex, Object-Oriented Programming (OOP) becomes essential. OOP is a way of organizing code that groups related data and functions together into objects. This allows you to manage larger programs more effectively, reducing duplication and improving scalability.

### Key Features of OOP:
- Classes and Objects: In OOP, you define a blueprint called a class, and from this blueprint, you can create multiple objects. Objects are instances of classes and hold both data and functions related to that data.
- Encapsulation: OOP bundles data (called attributes) and functions (called methods) together in an object, making it easier to manage and protect your data.
- Reusability: Through inheritance, you can create new classes based on existing ones, reducing code duplication.
- Scalability: OOP makes it easier to add new features without breaking existing code.



### Differences Between Procedural Programming and OOP

| Aspect                     | Procedural Programming                   | Object-Oriented Programming (OOP)         |
|----------------------------|------------------------------------------|------------------------------------------|
| **Basic Unit**              | Functions and Procedures                | Classes and Objects                       |
| **Data and Functions**      | Data and functions are separate         | Data and functions are bundled in objects |
| **Code Reusability**        | Limited code reusability                | High reusability through classes and inheritance |
| **Encapsulation**           | No encapsulation, data is exposed       | Data is encapsulated and protected        |
| **Complexity Management**   | Harder to manage as programs grow       | Easier to manage large programs with classes |
| **Code Duplication**        | Often leads to code duplication         | Reduces code duplication through inheritance and polymorphism |
| **Scalability**             | Not easily scalable for large programs  | Easily scalable by adding new classes or modifying existing ones |

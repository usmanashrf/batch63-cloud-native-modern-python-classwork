# Functions in Python
We've used functions many times, like `print()` and `input()`, to make tasks simpler. We've also worked with methods, which are special kinds of functions. Now, it's time to write our own functions, starting with simple ones and progressing to more complex examples.

## Why we need functions
Often, we'll find the same code repeating in our program with minor changes. Copying and pasting might seem convenient, but if an error occurs, fixing it everywhere can be tedious and risky. This is where functions come in. When a piece of code is repeated in multiple places, consider turning it into a function to streamline our code.

As programs grow, they can become difficult to manage. While comments help, too many make the code harder to follow. A well-written function should be concise and easily understood at a glance. Skilled developers break problems into small, isolated tasks, each handled by its own function, keeping the code clean and organized.

## Types of Functions
1. Built-in Functions:
    - We have already used python builtin functions e.g. `print()`, `input()`, `int()`, `float()`.
2. User defined Functions
    - User-defined functions are those functions which are defined by the user, for the user. 

## When to create a function
1. When a particular fragment of the code begins to appear in more than one place, consider the possibility of isolating it in the form of a function invoked.
2. When a piece of code becomes so large that reading and understating it may cause a problem, consider dividing it into separate, smaller
problems, and implement each of them in the form of a separate function.
3. Decompose the problem to allow the product to be implemented as a set of separately written functions packed together in different modules.

**Example**
```python
a : int = int(input("Enter a value"))
print(a)

b : int = int(input("Enter a value"))
print(b)

c : int = int(input("Enter a value"))
print(c)

```
We have written above example to get a number from user and print that number. We are doing this 3 times. 
This code is absolutely fine and will work. But what if our client/teacher asks as to print the number in this form. "User gave the number <number>".
So we have to change the print statement on multiple lines. 

In above example, we are repeating our code. We can use function here like so. 
```python
def print_number():
    a : int = int(input("Enter a value"))
    print(a)
```
Now see, we have to change the print on just a single line. Let's chage it as per client/teacher requirement.
```python
def print_number():
    a : int = int(input("Enter a value"))
    print(f"User gave the number {a}")
```

## How to create and use the function
For functions, we have to first define a function, then invoke (use) the function wherever it is required. 

**Step-1: Define (Create) a function**
Here is the syntax to create a function.
- We start from keyword `def`.
- Then we add function name. `def function_name`. The naming conventions for naming the functions is same as naming the variable in python.
- Then we add paranthesis `def function_name()`.
- And finally, we add colon `def function_name():`
- After the colon, comes our function body. Function body contains the code/logic of the task function in bening written for. 

Now our funciton has been defined. We can use it wherever we require.

**Step-2: Invoke (Use) a function**
We can use our function like so 
```python
function_name()
```
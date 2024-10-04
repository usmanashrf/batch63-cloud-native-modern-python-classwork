# Exception Handling in Python

When you're writing a program, things don't always go as planned. Sometimes, unexpected errors, called **exceptions**, can occur. If these exceptions are not handled properly, they will stop your program from running. This is where **exception handling** becomes crucial.

## What is an Exception?

An **exception** is an error that happens during the execution of a program. When an exception occurs, the normal flow of the program is interrupted, and the program will terminate unless you handle the exception.

There are many reasons an exception can occur:
- **Programming mistakes** (like dividing by zero)
- **Invalid user input** (like entering text where a number is expected)
- **External sources** (like trying to read from a file that doesn’t exist, network connection issues, database errors)

### Why is Exception Handling Important?

Without exception handling, even minor errors can cause your entire program to crash. By handling exceptions, you can:
1. **Prevent crashes**: You can ensure that your program continues to run or fails gracefully.
2. **Provide user feedback**: You can inform users about what went wrong instead of letting the program terminate abruptly.
3. **Debugging**: Proper exception handling helps identify where things went wrong, making it easier to debug your code.

---

### 1. **Basic `except` Block**
This will catch any error without specifying the type of exception. However, it’s not a good practice since it hides details of the error.

```python
def get_age():
    try:
        age = int(input("Enter your age: "))  # If input is not a number, this will raise an error
        print(f"Your age is: {age}")
    except:
        print("An error occurred")

get_age()
```
#### When to use:
- Rarely recommended. It catches **every type of exception**, including ones you may not want to catch (like `KeyboardInterrupt` or `SystemExit`). This can make debugging difficult because you don't get any information about what went wrong.

---

### 2. **Catching Specific Exceptions**
In this case, we specifically handle `ValueError` if the input is not a valid number.

```python
def get_age():
    try:
        age = int(input("Enter your age: "))  # If input is not a number, this will raise ValueError
        print(f"Your age is: {age}")
    except ValueError:
        print("Please enter a valid number for age")

get_age()
```
#### When to use:
- When you know what kind of exception could occur and want to handle that particular exception explicitly.
- It's good practice because you only catch exceptions you're prepared to handle.

---

### 3. **Catching Specific Exceptions and Accessing the Exception Object**
Here, we catch the specific `ValueError` and print the exact error message.
It also gives you access to the exception object to examine the error message or other details.

```python
def get_age():
    try:
        age = int(input("Enter your age: "))
        print(f"Your age is: {age}")
    except ValueError as e:
        print(f"Error occurred: {e}")

get_age()
```
#### When to use:
- When you need more information about the error to provide better debugging or logging information.
- Allows you to access the exception details for more refined error handling.

---

### 4. **Catching Multiple Exceptions**
We catch both `ValueError` and `TypeError` in this example. For instance, `TypeError` might occur if we pass a non-integer input.

```python
def add_numbers():
    try:
        a = int(input("Enter first number: "))
        b = input("Enter second number: ")
        print(a + b)  # This will raise TypeError because b is not converted to int
    except (ValueError, TypeError):
        print("An error occurred due to wrong input")

add_numbers()
```
#### When to use:
- When your code might raise different kinds of exceptions that need to be handled in the same way.
- It helps reduce repetitive code when handling multiple exceptions similarly.

---

### 5. **Catching Multiple Exceptions with Different Handlers**
We handle `ValueError` and `TypeError` differently in this case.

```python
def add_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))  # If not a number, this will raise ValueError
        print(a + b)
    except ValueError:
        print("Please enter valid numbers")
    except TypeError:
        print("There was a type error")

add_numbers()
```
#### When to use:
- When different types of exceptions require different handling.
- This makes your error handling more flexible and clear.

---

### 6. **Generic Exception Handling with `Exception`**
This catches any exception that is a subclass of `Exception` and prints the error message.
It is broader but doesn't catch system-exiting exceptions like `SystemExit` or `KeyboardInterrupt`.

```python
def add_numbers():
    try:
        a = int(input("Enter first number: "))
        b = input("Enter second number: ")
        print(a + b)  # This will cause a TypeError
    except Exception as e:
        print(f"An error occurred: {e}")

add_numbers()
```
#### When to use:
- If you want to handle **most exceptions** but not system-level exceptions like program exit signals.
- It’s useful for logging or generic error handling while still keeping critical exceptions like `KeyboardInterrupt` uncaught.

---

### 7. **`finally` Block**
The `finally` block always runs whether there’s an exception or not. It’s useful for cleanup tasks, like closing files.

```python
def divide_numbers():
    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        print(a / b)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    finally:
        print("Thank you for using the division program")

divide_numbers()
```
#### When to use:
- When you have some code that **must run no matter what**, such as releasing resources or cleaning up after the `try` block (e.g., closing a file or a network connection).

---

### 8. **Using `else` Block**
The `else` block executes only if no exceptions occur in the `try` block.

```python
def divide_numbers():
    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"Division successful: {result}")

divide_numbers()
```
#### When to use:
- When you have code that should only run **if no exceptions were raised**. This makes your intentions clear and keeps your code cleaner.

---

### 9. **Re-raising Exceptions**
You can catch the exception, do something (like logging), and then re-raise it for further handling or to stop the program.

```python
def divide_numbers():
    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        print(a / b)
    except ZeroDivisionError as e:
        print(f"Caught a ZeroDivisionError: {e}")
        raise  # Re-raise the exception

divide_numbers()
```
#### When to use:
- When you want to handle an exception temporarily (like logging or cleaning up) but still want to **pass it up** the call stack for further handling.

---

### 10. **Chaining Exceptions with `raise ... from`**
Here we catch one error (e.g., `ZeroDivisionError`) and raise a different exception while keeping the original context.

```python
def divide_numbers():
    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        print(a / b)
    except ZeroDivisionError as e:
        raise ValueError("Invalid input for division") from e

divide_numbers()
```
#### When to use:
- When handling one type of exception but want to transform it into a different exception while keeping the context of the original error. This can be useful for debugging.

---



### 6. **Generic Exception Handling with `Exception`**
This catches all exceptions that are subclasses of `Exception`. It is broader but doesn't catch system-exiting exceptions like `SystemExit` or `KeyboardInterrupt`.

```python
try:
    # some code
except Exception as e:
    print(f"An error occurred: {e}")
```



### 7. **`finally` Block**
This is used to execute code regardless of whether an exception occurred or not. The `finally` block is often used for cleanup actions like closing files or releasing resources.

```python
try:
    # some code
except ValueError:
    print("A ValueError occurred")
finally:
    print("This will always execute")
```



### 8. **Using `else` Block**
The `else` block executes only if no exception was raised in the `try` block.

```python
try:
    # some code
except ValueError:
    print("A ValueError occurred")
else:
    print("No exceptions occurred")
```


### 9. **Chaining Exceptions with `raise ... from`**
This allows you to raise a new exception while preserving the context of the original exception.

```python
try:
    # some code
except ValueError as e:
    raise TypeError("A different error occurred") from e
```
---

### Key Take aways:
- The except branches are searched in the same order in which they appear in the code;
- You must not use more than one except branch with a certain exception name;
- The number of different except branches is arbitrary - the only condition is that if you use try, you must put at least one except (named or not) after it;
- The except keyword must not be used without a preceding try;
- If any of the except branches is executed, no other branches will be visited;
- If none of the specified except branches matches the raised exception, the exception remains unhandled (we'll discuss it soon)
- If an unnamed except branch exists (one without an exception name), it has to be specified as the last.

---

### Why Do Exceptions Increase Execution Time?

1. **Exceptions Are Meant for Uncommon Situations**: 
   - Exceptions are designed to handle unexpected or rare situations in your program, not for normal control flow.
   - Python's exception-handling mechanism involves setting up the `try-except` blocks, and when an exception is raised, the interpreter needs to unwind the call stack, look for the matching `except` block, and jump there. This entire process is slower compared to using regular conditionals (`if-else`) to handle predictable situations.

2. **Handling Exceptions Is More Expensive**:
   - The cost of handling an exception is higher than simply performing a regular check (like using `if` statements) because of the extra overhead in managing stack frames and control flow changes.
   - For example, if you use `try-except` for controlling the flow of your program in situations where simple checks could be done, it can make your code less efficient.

### Example: Using Exceptions vs. Conditionals

Let’s consider two ways to check for an invalid input:

1. **Using Exceptions**:
   ```python
   def divide(a, b):
       try:
           result = a / b
           return result
       except ZeroDivisionError:
           return "Cannot divide by zero!"
   ```

2. **Using Conditionals**:
   ```python
   def divide(a, b):
       if b == 0:
           return "Cannot divide by zero!"
       else:
           return a / b
   ```

In the second example, we avoid raising and handling an exception by checking if the divisor is zero before performing the operation. This is typically faster, especially when the operation is part of a loop or frequently called function.

### When to Use Exceptions?

- **Exceptions should be used for truly exceptional circumstances**, where errors are unlikely to occur and are difficult to predict or check for upfront (e.g., reading from a file that might not exist, network timeouts, database failures).
- **Use conditionals** (like `if-else`) for scenarios where errors can be easily anticipated or checked beforehand. This way, you avoid the performance overhead of handling exceptions.

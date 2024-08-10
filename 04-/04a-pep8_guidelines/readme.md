# PEP 8 Guidelines

## A- PEP 8 Variable Naming Conventions

PEP 8 provides several guidelines for naming variables, which help maintain consistency and readability in Python code. Here are the main variable naming conventions as specified by PEP 8:

### 1. **Descriptive Naming**

- Variable names should be descriptive and meaningful.

```python
count = 0
total_price = 100.50
```

### 2. Lowercase with Underscores

- Variable names should be in lowercase and words should be separated by underscores.

```python
user_name = "JohnDoe"
item_count = 42
```

### 3. Avoid Single Character Names

- Avoid using single character names except for loop counters or in very short blocks.

````python
for i in range(10):
  print(i)
  ```
### 4. Constants in All Capitals
- Constants should be written in all capital letters with underscores separating words.
```python
MAX_CONNECTIONS = 100
PI = 3.14159
````

### 5. Class Names

- Class names should follow the CapWords convention (also known as PascalCase).

```python
class MyClass:
  pass


class EmployeeRecord:
  pass
```

### 6. Instance and Class Variables

- Instance variables should follow the same lowercase with underscores convention.
- Class variables should be capitalized if they are constants.

```python
class ExampleClass:
  class_variable = 0

  def __init__(self, value):
      self.instance_variable = value
```

### 7. Function and Method Names

- Function and method names should be lowercase, with words separated by underscores as necessary to improve readability.

```python
def my_function():
  pass

class MyClass:
    def my_method(self):
        pass
```

### 8. Private Variables

- Use a leading underscore to indicate a private variable.

```python
_private_variable = 42

class MyClass:
    def __init__(self):
        self._private_instance_variable = "private"

```

### 9. Avoid Trailing Underscores

- Avoid using trailing underscores in variable names.

```python
# Use class_ instead of class which is a keyword
class_ = "Math"

```

### 10. Double Leading Underscores

- Use double leading underscores to invoke name mangling.

```python
class MyClass:
  def __init__(self):
      self.__mangled_name = "mangled"
```

### 11. Variables with Special Meanings

- Follow the naming conventions for variables with special meanings (e.g., **all**, **author**, **version**).

```python
__all__ = ['module1', 'module2']
__version__ = '1.0'
__author__ = 'Your Name'

```

## B- Indentation and Line Length

1. **Indentation**

   - Use 4 spaces per indentation level.
     ```python
     def example_function():
         a = 5
         b = 10
         return a + b
     ```
     ```python
     if True:
         print("Hello, World!")
     ```

2. **Maximum Line Length**

   - Limit all lines to a maximum of 79 characters.
     ```python
     def example_function_with_long_name(argument_one, argument_two, argument_three):
         return argument_one + argument_two + argument_three
     ```
     ```python
     long_variable_name = "This is a very long string that goes beyond the limit of 79 characters."
     ```

3. **Blank Lines**

   - Surround top-level function and class definitions with two blank lines.
   - Method definitions inside a class are surrounded by a single blank line.

     ```python
     class MyClass:

         def method_one(self):
             pass

         def method_two(self):
             pass
     ```

     ```python
     def function_one():
         pass


     def function_two():
         pass
     ```

## C- Imports

4. **Imports**
   - Imports should usually be on separate lines.
   - Imports should be grouped in the following order: standard library imports, related third-party imports, local application/library-specific imports.
     ```python
     import os
     import sys
     ```
     ```python
     from subprocess import Popen, PIPE
     from mymodule import my_function
     ```

## D- String Quotes

5. **String Quotes**
   - In a Python program, pick a rule and stick to it. Single or double quotes are acceptable.
     ```python
     my_string = "Hello, World!"
     another_string = 'Hello, World!'
     ```

## E- Whitespace

6. **Whitespace in Expressions and Statements**

   - Avoid extraneous whitespace in the following situations.

     ```python
     # Correct:
     x = 1
     y = 2
     long_variable = 3

     # Incorrect:
     x             = 1
     y             = 2
     long_variable = 3
     ```

## F- Comments

7. **Comments**

   - Comments should be complete sentences. Use a capital letter to start the comment, and end it with a period.

     ```python
     # This is a correct comment.
     a = 5  # This is an inline comment.

     # incorrect comments.
     a = 5  # this is an incorrect comment
     ```

## G- Naming Conventions

8. **Naming Conventions**

   - Follow standard naming conventions: function names, variable names, and filenames should be lowercase with words separated by underscores as necessary to improve readability.

     ```python
     def my_function():
         pass

     variable_name = 10
     ```

## H- Programming Recommendations

9. **Programming Recommendations**

   - Always use `def` for creating functions, not `lambda` for assignments.

     ```python
     def add(x, y):
         return x + y

     # Instead of:
     add = lambda x, y: x + y
     ```

10. **Module Level Dunder Names**

- Module level "dunders" (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring and before any import statements except `from __future__` imports.

  ```python
  """Module docstring."""

  __all__ = ['foo', 'bar']
  __version__ = '1.0'
  __author__ = 'Your Name'

  import os
  import sys
  ```

11. **Top-level Script Environment**

- Always use `if __name__ == "__main__":` construct for top-level script environment.

  ```python
  def main():
      print("Hello, World!")

  if __name__ == "__main__":
      main()
  ```

12. **Trailing Commas**

- Avoid using trailing commas in a list.

  ```python
  my_list = [
      1,
      2,
      3,
  ]

  # Correct:
  my_list = [1, 2, 3]
  ```

13. **Method Definitions**

- Always use `self` as the first argument in instance methods.
  ```python
  class MyClass:
      def method(self):
          pass
  ```

## I-Line Breaks and Statements

14. **Line Breaks**

- Use backslashes for line continuation if needed.
  ```python
  total = item_one + item_two + item_three + \
          item_four + item_five
  ```

15. **Compound Statements**

- Avoid using compound statements (multiple statements on the same line).

  ```python
  # Correct:
  if foo == 'bar':
      do_something()

  # Incorrect:
  if foo == 'bar': do_something()
  ```

## J- Accessing Names

16. **Accessing Names in a Module**

- Use absolute imports whenever possible.
  ```python
  import mypkg.sibling
  from mypkg import sibling
  from mypkg.sibling import example_function
  ```

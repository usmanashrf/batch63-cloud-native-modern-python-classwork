# Lambda Functions in Python

In Python, **lambda functions** are anonymous, inline functions that can have any number of arguments but only a single expression. They are often used for simple operations and as a shorthand in situations where defining a full function would be unnecessary or cumbersome.

## What is a Lambda Function?

A **lambda function** in Python is a small anonymous function defined with the `lambda` keyword. Unlike regular functions defined using `def`, a lambda function is a single expression. Lambda functions are often used as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

### Key Points:

- **Anonymous**: Lambda functions are not bound to a name, hence they're referred to as anonymous functions.
- **Single expression**: They contain only one expression and automatically return the result of that expression.
- **Inline**: They are often used inline and passed as arguments to functions.

---

## Syntax of a Lambda Function

The syntax of a lambda function is straightforward:

```python
lambda arguments: expression
```

- **`lambda`**: The keyword used to define a lambda function.
- **`arguments`**: A comma-separated list of parameters (just like a normal function).
- **`expression`**: A single expression that is evaluated and returned.

### Example of Lambda Syntax:

```python
# A lambda function that adds 10 to a number
add_ten = lambda x: x + 10

# Call the lambda function
print(add_ten(5))  # Output: 15
```

---

## Examples of Lambda Functions

### Example 1: Basic Lambda Function

A simple lambda function that takes one argument and returns its square.

```python
# Lambda function to square a number
square = lambda x: x * x

print(square(4))  # Output: 16
```

### Example 2: Lambda with Multiple Arguments

Lambda functions can take multiple arguments just like regular functions.

```python
# Lambda function to multiply two numbers
multiply = lambda a, b: a * b

print(multiply(3, 5))  # Output: 15
```

### Example 3: Using Lambda with Built-in Functions

Lambda functions are commonly used with Python’s built-in higher-order functions like `map()`, `filter()`, and `sorted()`.

#### `map()` with Lambda:

`map()` applies a lambda function to each item in a list or iterable.

```python
numbers = [1, 2, 3, 4, 5]

# Square each number using map and lambda
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

#### `filter()` with Lambda:

`filter()` returns elements of a list that satisfy a given condition (lambda function).

```python
numbers = [1, 2, 3, 4, 5, 6]

# Filter out even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]
```

#### `sorted()` with Lambda:

`sorted()` can use a lambda function as a `key` to sort based on custom criteria.

```python
students = [("Ali", 85), ("Zara", 90), ("Bob", 75)]

# Sort by student scores (second item in tuple)
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)  # Output: [('Bob', 75), ('Ali', 85), ('Zara', 90)]
```

---

## Use Cases for Lambda Functions

1. **Simple Operations**: Lambda functions are ideal for small, simple operations where defining a full `def` function would be unnecessary.

   Example: Applying a simple mathematical operation inline:

   ```python
   add_five = lambda x: x + 5
   print(add_five(10))  # Output: 15
   ```

2. **Higher-Order Functions**: When working with functions like `map()`, `filter()`, and `reduce()`, lambda functions provide a concise and readable way to pass behavior to the function.
3. **Sorting**: Lambda functions are often used with the `sorted()` function to customize sorting based on specific fields.

4. **Functional Programming**: Lambdas are useful in functional programming patterns where functions are passed as arguments or returned from other functions.

---

## Limitations of Lambda Functions

1. **Single Expression**: Lambda functions are limited to one expression, which can sometimes make them less readable if complex logic is required.
2. **No Statements**: Unlike normal functions, lambda functions can't contain statements such as loops, print, or multi-line logic.

3. **Less Readable for Complex Operations**: While lambda functions are concise, they can reduce readability if overused or used for complex logic.

4. **No Annotations**: Lambda functions don't support function annotations (type hints).

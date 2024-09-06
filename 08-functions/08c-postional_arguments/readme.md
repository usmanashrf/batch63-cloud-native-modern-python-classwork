# Positional Arguments in Python Functions
When defining a function, we can specify parameters that act as placeholders for values the function will receive. These values, called **arguments**, are passed when we call the function.

One common way to pass arguments is using **positional arguments**. This means the arguments are assigned to parameters based on their position in the function call.


## What Are Positional Arguments?

Positional arguments are arguments that are passed to a function based on the order they appear in the function call. The first argument is assigned to the first parameter, the second to the second parameter, and so on.

### Syntax:
```python
def function_name(parameter1, parameter2, ...):
    print(f"Parameter 1: {parameter1}")
    print(f"Parameter 2: {parameter2}")
    return parameter1-parameter2
```

When calling the function, we pass values for each parameter in the same order as they were defined.

```python
function_name(argument1, argument2, ...)
```

---

## How Positional Arguments Work

The following example illustrates a function that uses positional arguments:

```python
def greet(name, message):
    print(f"Hello {name}, {message}")

greet("Ali", "Welcome to Python!")  # Output: Hello Ali, Welcome to Python!
```

In the example:
- `"Ali"` is passed as the first argument and is assigned to the `name` parameter.
- `"Welcome to Python!"` is passed as the second argument and is assigned to the `message` parameter.

The position of the arguments is crucial here. If we change the order, the meaning of the arguments changes.

```python
greet("Welcome to Python!", "Ali")  # Output: Hello Welcome to Python!, Alice
```

---

## Examples of Positional Arguments

Here are some more examples to demonstrate how positional arguments work:

### Example 1: A Function with Two Parameters

```python
def add_numbers(a, b):
    return a - b

result = add_numbers(10, 5)
print(result)  # Output: 5
```

In this example, `10` is passed to the parameter `a` and `5` is passed to `b`. The difference of the two is returned.
However, we the result will be changed if we pass the parameter in opposite order. Do check that out. So the order is crucial in positional arguments.

### Example 2: Function with Three Positional Arguments

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("Musa", 25, "New York")
# Output: Musa is 25 years old and lives in New York.
```

Here, the arguments are passed in the order corresponding to the parameters: `name`, `age`, and `city`.

---

## Multiple Positional Arguments

We can pass any number of positional arguments to a function as long as they match the number of parameters defined in the function defination.

### Example 3: Function with Multiple Parameters

```python
def multiply(x, y, z):
    return x * y * z

result = multiply(2, 3, 4)
print(result)  # Output: 24
```

The function `multiply` accepts three positional arguments, and the result is the product of the three numbers.

---

## Best Practices for Positional Arguments

- **Order Matters**: Since the arguments are mapped to parameters based on their position, always ensure they are passed in the correct order.
  
- **Matching Parameters**: Ensure that the number of arguments matches the number of parameters in the function definition. If the numbers don’t match, Python will raise an error.

```python
def subtract(a, b):
    return a - b

# Correct usage
print(subtract(10, 5))  # Output: 5

# Incorrect usage
# print(subtract(10))  # Error: subtract() missing 1 required positional argument: 'b'
```

- **Readability**: It’s essential to pass arguments in a way that makes the function call readable and understandable.

---

## Conclusion

Positional arguments in Python allow us to pass values to a function in a straightforward manner, based on their position. Understanding how to use positional arguments effectively is crucial when writing clean, functional Python code. Just remember that order matters, and the number of arguments must match the function’s parameter list.

For more advanced functionality, Python also supports keyword arguments, default arguments, and variable-length arguments (`*args` and `**kwargs`), but positional arguments are the foundation of function calls in Python. We will see `*args` and `**kwargs` in coming sections.

---


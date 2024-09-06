# `*args` and `**kwargs` in Python Functions

Python functions allow for a wide range of flexibility when it comes to passing arguments. Two powerful features of Python are `*args` and `**kwargs`, which let us pass a variable number of arguments to a function. These features give developers more control and flexibility over how functions handle data.


## What are `*args` and `**kwargs`?

- **`*args`**: Allows a function to accept any number of positional arguments as a tuple.
- **`**kwargs`**: Allows a function to accept any number of keyword arguments as a dictionary.

These features provide flexibility when we don’t know in advance how many arguments will be passed to our function.

---

## How `*args` Work

When a function has `*args` as a parameter, it can accept any number of positional arguments. Inside the function, these arguments are available as a tuple.

### Syntax:
```python
def function_name(*args):
    # args is a tuple containing all positional arguments
    for arg in args:
        print(arg)
```

### Example:
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(4, 5, 6, 7))  # Output: 22
```

In this example, the function `sum_numbers` accepts any number of positional arguments and returns their sum.

---

## How `**kwargs` Work

When a function has `**kwargs` as a parameter, it can accept any number of keyword arguments. Inside the function, these arguments are available as a dictionary where the keys are the argument names and the values are the corresponding values.

### Syntax:
```python
def function_name(**kwargs):
    # kwargs is a dictionary containing all keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### Example:
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25, city="New York")
# Output:
# name: Ali
# age: 25
# city: New York
```

In this example, `print_info` accepts any number of keyword arguments and prints them.

---

## Examples of Using `*args`

### Example 1: A Function with Multiple Positional Arguments

```python
def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_numbers(2, 3, 4))  # Output: 24
print(multiply_numbers(1, 5, 10))  # Output: 50
```

In this function, `multiply_numbers` can accept a variable number of arguments and multiply them together.

### Example 2: Passing a List as `*args`

We can also pass a list of arguments using the `*` operator.

```python
numbers = [1, 2, 3, 4]
print(multiply_numbers(*numbers))  # Output: 24
```

Here, the list `numbers` is unpacked into positional arguments using `*`.

---

## Examples of Using `**kwargs`

### Example 1: Function with Multiple Keyword Arguments

```python
def greet(**kwargs):
    if 'name' in kwargs:
        print(f"Hello {kwargs['name']}!")
    else:
        print("Hello Guest!")

greet(name="Bob")  # Output: Hello Bob!
greet()  # Output: Hello Guest!
```

In this example, `greet` can accept any number of keyword arguments and checks if a `name` argument is provided.

### Example 2: Passing a Dictionary as `**kwargs`

We can pass a dictionary of keyword arguments using the `**` operator.

```python
person_info = {"name": "Ali", "age": 30}
greet(**person_info)  # Output: Hello Ali!
```

The dictionary `person_info` is unpacked and passed as keyword arguments to the `greet` function.

---

## Combining `*args` and `**kwargs`

We can use both `*args` and `**kwargs` in the same function to handle a combination of positional and keyword arguments.

### Example 1: Handling Both Positional and Keyword Arguments

```python
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Ali", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Ali', 'age': 25}
```

In this example, `display_info` accepts both positional and keyword arguments and prints them separately.

### Example 2: Function with Default Arguments, `*args`, and `**kwargs`

```python
def order_pizza(size="medium", *toppings, **details):
    print(f"Size: {size}")
    print(f"Toppings: {', '.join(toppings)}")
    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

order_pizza("large", "pepperoni", "mushrooms", name="Ali", delivery_time="18:00")
# Output:
# Size: large
# Toppings: pepperoni, mushrooms
# Details:
#   name: Ali
#   delivery_time: 18:00
```

In this example, `order_pizza` accepts a default argument, multiple toppings as `*args`, and order details as `**kwargs`.

---

## Best Practices for `*args` and `**kwargs`

1. **Use `*args` for unknown number of positional arguments**: Use `*args` when you don’t know how many positional arguments will be passed to your function.
2. **Use `**kwargs` for optional keyword arguments**: Use `**kwargs` when you want to allow optional keyword arguments.
3. **Order matters**: When defining a function with both `*args` and `**kwargs`, the order should be: positional arguments, `*args`, default parameters, and then `**kwargs`.
4. **Descriptive variable names**: While `*args` and `**kwargs` are the convention, you can give them more descriptive names like `*numbers` or `**options` to improve readability.




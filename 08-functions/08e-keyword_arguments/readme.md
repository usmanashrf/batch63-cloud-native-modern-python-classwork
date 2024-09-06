# Keyword Arguments in Python Functions

In Python, **keyword arguments**, allow us to pass arguments by explicitly specifying the parameter name. This is in contrast to **positional arguments**, where the position of the argument in the function call determines which parameter it will be assigned to.

## What Are Keyword Arguments?

Keyword arguments are passed to a function using the syntax `parameter_name=value`. Unlike positional arguments, the order of the arguments doesn't matter, as each one is explicitly assigned to a parameter by name.

### Syntax:
```python
def function_name(parameter1, parameter2, ...):
    # function body
    return something

function_name(parameter1=value1, parameter2=value2, ...)
```

By using keyword arguments, you can make function calls more readable and flexible.

---

## How Keyword Arguments Work

The following example illustrates a function that uses keyword arguments:

```python
def greet(name, message):
    print(f"Hello {name}, {message}")

greet(name="Ali", message="Welcome to Python!")  # Output: Hello Ali, Welcome to Python!
```

In this case:
- The argument `name` is assigned the value `"Ali"`.
- The argument `message` is assigned `"Welcome to Python!"`.

Even though the parameters were defined in a specific order in the function definition, we can pass the arguments in any order as long as the names match:

```python
greet(message="Welcome to Python!", name="Ali")  # Output: Hello Ali, Welcome to Python!
```
If we do not use keyword argument and change the position, our output will be changed. But if we use keyword argument, we can use any order.

---

## Examples of Keyword Arguments

Here are some examples to demonstrate how keyword arguments can be used:

### Example 1: Using Keyword Arguments

```python
def book_info(title, author, year):
    print(f"'{title}' by {author}, published in {year}")

book_info(title="1984", author="George Orwell", year=1949)
# Output: '1984' by George Orwell, published in 1949
```

### Example 2: Using Default Parameter Values and Overriding with Keyword Arguments

We can assign default values to parameters, and only provide values for those we want to override using keyword arguments.

```python
def greet(name="Guest", message="Welcome!"):
    print(f"Hello {name}, {message}")


greet()  # Output: Hello Guest, Welcome!

greet(name="Ali")  # Output: Hello Ali, Welcome!

greet(message="Good morning!")  # Output: Hello Guest, Good morning!

greet(name="Ali", message="Good morning!")  # Output: Hello Ali, Good morning!
```

In this example:
- If no arguments are passed, the default values `"Guest"` and `"Welcome!"` are used.

- If a keyword argument is provided, it overrides the default.

---

## Using Positional and Keyword Arguments Together

We can combine both positional and keyword arguments in a function call. However, there are a few important rules:
1. Positional arguments must come before keyword arguments.
2. Once we use a keyword argument, all subsequent arguments must also be keyword arguments.

### Example 3: Combining Positional and Keyword Arguments

```python
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional argument for pet_name, keyword argument for animal_type
describe_pet("Tickle", animal_type="cat")
# Output: I have a cat named Tickle.

# Positional argument for both parameters
describe_pet("Max", "dog")
# Output: I have a dog named Max.

# Keyword arguments for both
describe_pet(animal_type="duck", pet_name="i forgot")
# Output: I have a duck named i forgot.
```

### Example 4: Mixed Positional and Keyword Arguments

```python
def order_drink(drink, size="medium", sugar="regular"):
    print(f"Order: {size} {drink} with {sugar} sugar.")

# Positional for 'drink', keyword for others
order_drink("coffee", size="large", sugar="no")
# Output: Order: large coffee with no sugar.
```

---

## Best Practices for Keyword Arguments

- **Improves Readability**: When calling functions with multiple arguments, use keyword arguments for clarity, especially if some arguments have default values that don’t need to be overridden.

- **Use Defaults**: If a function has parameters with default values, make use of keyword arguments to override only the ones that need to be changed, and keep the rest as default.

- **Combine with Positional Arguments**: Positional arguments should be used when the parameters are obvious (like the first few parameters of a function), and keyword arguments can be used for optional or less frequently changed parameters.

```python
def make_pizza(size, topping="cheese", crust="thin"):
    print(f"{size} pizza with {topping} and {crust} crust")

# Clear and readable
make_pizza("large", crust="stuffed")
# Output: large pizza with cheese and stuffed crust
```



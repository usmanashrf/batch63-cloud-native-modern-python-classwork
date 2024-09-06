# Scopes in Python
The scope of variable in python is an environment where it can be recognizable. 
For example, the scope of parameter is always inside the function. 

**Example:**

```python
def greetings(name):
    print(name)

greetings("Rehan")
```
In above example, the scope of parameter `name` is only inside the function. If we try to use it outside the function, it will generate error. 

Let's try it.

```python
def greetings(name):
    print(name)

greetings("Rehan")
print(name) # NameError: name 'name' is not defined
```

**The variable existing outside the function has a global scope. Means, it can be accessed inside the function.** 

**Example:**
```python
my_name : str = "Musa"

def greetings():
    print(f"Hello {my_name}")

greetings() # Output: Hello Musa
```

**What if variable existing outside the function has the same name as the parameter of the function?**

```python
name : str = "Musa"
def greetings(name):
    print(f"Name Inside Function: {name}")

greetings("Rehan")
print(f"Name Outside Function:{name}")

```
or 

```python
name : str = "Musa"
def greetings():
    name = "Rehan"
    print(f"Name Inside Function: {name}")

greetings()
print(f"Name Outside Function:{name}")

```
In above example, we are using same variable `name` inside and outside the function. The results conclude the followings. 
- Parameters doesn't exist outside the function.
- If the name of the variable is same, the python is intelligent enough to differentiate it. 
- It will print the value provided as argument (parameter value) inside the function and outside the function, it will print the value of the variable exisiting outside the funciton.

## The `global` keyword
We can declare a variable outside the function and access it inside the function with `global` keyword.

```python
teacher_name : str = "Usman"

def greetings():
    global teacher_name
    teacher_name = "Rehan"
    print(f"Inside Function: {teacher_name}")

greetings()

print(f"Outside the Function: {teacher_name}")

```

## Important Points
### For Immutable Types
- Changing the parameter's value doesn't propagate outside the
function (in any case, not when the variable is a scalar (primitive)).

- This also means that a function receives the argument's value, not the argument itself.

```python
def any_function (value):
    print(f"value Received: {value}")
    value += 100
    print(f"value changed inside func : {value}")

value = 4
any_function(value)
print(f"Value outside the func: {value}")

```
### For Mutable Types
But for lists, a case is bit different. Let's learn from same example but instead we'll use lists.

```python
def any_function (num_list):
    print(f"value Received: {num_list}")
    num_list.append(500)
    print(f"num_list changed inside func : {num_list}")

num_list = [1, 2, 4, 5]
any_function(num_list)
print(f"num_list outside the func: {num_list}")
```
#### Explanation:
- When a scalar is passed to a function, Python creates a copy of the value (since they are immutable). Any modifications inside the function will be applied to the local copy, and the original variable outside the function remains unchanged.

- In contrast, if the function were modifying a mutable object like a list or dictionary, the changes would be reflected outside the function. This is because mutables are passed by reference, and their internal state can be altered without creating a new copy.
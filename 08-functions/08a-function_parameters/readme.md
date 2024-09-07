# Function Parameters
In this section, we'll learn about parameterless and parameterized functions. 

## What are function parameters?
So far we learnt that functions perform a specific task. To perform the task, in some cases, function needs some inputs/data and in other cases, it doesn't.
- Parameters simply can be said the inputs/data required by the function to perform a specific task. 
- The inputs/data is provided from outside the function but we have to mention them while defining the functions. 
- Parameters only exist inside the function.
- parameters are provided in paranthesis of the function. 

Let's have a look at parameterless and parameterized function.

## Parameterless Fucntions:
These type of functions don't require parameters.

```python
def greetings():
    print("Hello Rehan!")

greetings() #Output: Hello Rehan!
```

## Parameterized Fucntions:
These type of functions require parameters.

```python
my_name : str = "Rehan"
def greetings(name):
    print(f"Hello {name}!")

greetings(my_name) #Output: Hello Rehan!
```
- `name` here, is the parameter provided to the function. 
- Now our function has become more dynamic. We can provide any name, it will greet that person.
- `my_name` is the argument provided at the time of function invokation.

## What are Arguments?
Arguments are the actual values you pass to a function when you call it. These values get assigned to the function’s parameters.

```python
greetings("Rehan") 
```
`Rehan` is the argument provided to the function. 
- Arguments live outside the function.
- Arguments can be accessed inside the function. 
**Parameters**
- Parameters are defined in function at the time of function definition.
- Parameters only live inside function. They don't have outside scope.

We'll discuss it in details in `Scope` section.

# Function Return
## 1. Reutrn with expression
So far we only discussed the functions which perform specific task but do not provide results. Now we'll discuss the functions which do provide a result and we get this result through `return` keyword. 

Let's look at example of a function which takes 2 parameters (numbers), add them (perform a task) and return the result. 

```python
# Define a function
def addition(first_number:int, second_number:int)->int:
    result : int = first_number + second_number
    return result


print(addition(5, 8)) # Output: 13
# Can also do like this
get_sum : int = addition(5,8)
print(get_sum) #Output: 13

```
If we take example of python builin functions, `print()` function doesn't return anything while `int()` returns and integer value. 

Here we are using return with expression. `return result` here 'result' is the expression.

## 2. Reutrn without expression
Sometimes, we use `return` keyword without expression. What will function return in that case. Well, function will then return `None` 

**Usecase**
In above example, we were just getting the sum of 2 numbers. Let's add a scenarion. We want our function to add the value only when both of the numbers are non zero. Let's implement it inside the function.

```python
# Define a function
def addition_non_zero(first_number:int, second_number:int)->int | None:
    if first_number > 0 and second_number > 0:
        result : int = first_number + second_number
        return result


get_sum : int | None = addition_non_zero(5,8)
print(get_sum) # Output: 13

get_sum : int | None = addition_non_zero(0,8)
print(get_sum) # Output: None

```

## 3. Return Multiple values
Remember, function will always return a single value. So how can we return if we need multiple values. We use tuple in that case. Function still returns a single value (a tuple), but we already know that we can unpack the tuple. 

**Example**
```python
def mul_and_add(a:int, b:int)-> tuple[int, int]:
    multiplication : int = a * b
    addition : int = a + b
    return multiplication, addition

result = mul_and_add(5, 4)
print(result)  # Output: (20, 9)

# We can unpack it like so
mul_result, add_result = mul_and_add(5, 4)
print(f"Multiplication result:{mul_result}")
print(f"Addition result:{add_result}")
```

## 4. Return a list

```python
def generate_even_numbers(limit):
    even_numbers = [i for i in range(limit) if i % 2 == 0]
    return even_numbers

result = generate_even_numbers(10)
print(result)  # Output: [0, 2, 4, 6, 8]
```

## 5. Return a dictionary
```python
def get_student_info(name, age, course):
    return {
        "name": name,
        "age": age,
        "course": course
    }

student_info = get_student_info("John", 21, "Mathematics")
print(student_info)  # Output: {'name': 'John', 'age': 21, 'course': 'Mathematics'}
```
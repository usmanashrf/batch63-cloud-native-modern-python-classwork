# Modules in Python

## Understanding Growing Code and the Need for Modules

**1. Code Growth and User Expectations:**
As users' needs evolve, so must the code. Any widely-used program will continually change to meet new demands. Unresponsive code becomes obsolete.

**2. Growing Code = Growing Complexity:**
Larger codebases are harder to maintain. Bugs are easier to spot in smaller, simpler programs, so as code grows, it requires better organization.

**3. Why Split Code into Parts?**
For large projects with many developers, it's impractical for everyone to work on the same file. Dividing the code into manageable parts is essential to avoid confusion and errors.


**4. Modules: The Solution**
To manage complexity, Python uses **modules**. A module is a file containing Python code that can be reused. It allows you to divide your program into smaller, manageable pieces.



1. **What is a Module?**  
   A module is a Python file that contains functions, classes, or variables. You can import it into other Python files to reuse its code.

2. **Why Use Modules?**  
   Modules help organize code, make it reusable, and improve maintainability by separating functionality.

3. **How to Create and Use Modules:**  
   - Save your Python code in a `.py` file. For example, `math_utils.py`.
   - Use `import` to include this module in another file.

## Example

**Creating a Module:**
```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**Using the Module in Another File:**
```python
# main.py
import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8
```
## Usage Examples


1. **`import math`**  
   In this case, you import the entire `math` module and can use its functions with the `math.` prefix.

   ```python
   import math
   
   # Example usage
   result = math.sqrt(16)  # Using the sqrt function from math module
   print(result)  # Output: 4.0
   ```

2. **`import module1, module2, module3`**  
   Here you import multiple custom modules (`module1`, `module2`, `module3`). Assuming these modules exist, you would use them similarly with the module name prefix.

   ```python
   import module1, module2, module3
   
   # Example usage (assuming the modules have relevant functions)
   module1.function1()
   module2.function2()
   module3.function3()
   ```

3. **`from math import sin`**  
   You are importing only the `sin` function from the `math` module, and can use it directly without the `math.` prefix.

   ```python
   from math import sin
   
   # Example usage
   result = sin(math.pi / 2)  # Using sin directly
   print(result)  # Output: 1.0
   ```

4. **`from math import sin, pi`**  
   You are importing both `sin` and `pi` from the `math` module and can use them directly without the `math.` prefix.

   ```python
   from math import sin, pi
   
   # Example usage
   result = sin(pi / 2)
   print(result)  # Output: 1.0
   ```

5. **`from math import *`**  
   This imports everything from the `math` module, so you can access all functions and constants directly.

   ```python
   from math import *
   
   # Example usage
   result1 = sqrt(16)  # Using sqrt directly
   result2 = cos(pi)   # Using cos and pi directly
   print(result1, result2)  # Output: 4.0 -1.0
   ```

6. **`import math as rehan`**  
   Here you are importing the `math` module with an alias `rehan`, and can use it with the alias instead of `math`.

   ```python
   import math as rehan
   
   # Example usage
   result = rehan.sqrt(16)  # Using the sqrt function with the alias
   print(result)  # Output: 4.0
   ```

7. **`from math import sin as sine_funct`**  
   You are importing the `sin` function and giving it an alias `sine_funct`, so you can use the alias instead of `sin`.

   ```python
   from math import sin as sine_funct
   
   # Example usage
   result = sine_funct(math.pi / 2)  # Using the sin function as sine_funct
   print(result)  # Output: 1.0
   ```

## `if__name__ == "__main__":` Construct

The `if __name__ == "__main__":` construct is a common Python idiom used to control whether certain parts of the code are executed when the script is run directly, as opposed to when it is imported as a module in another script.

### Explanation of `if __name__ == "__main__":`

1. **`__name__` Variable**:
   - In Python, the `__name__` variable is automatically set by the interpreter. When a Python file is executed, `__name__` is set to `"__main__"`.
   - If the file is imported as a module in another file, `__name__` will be set to the name of the file (the module name), without the `.py` extension.

2. **`if __name__ == "__main__":` Check**:
   - This check ensures that a block of code is only executed when the file is run directly (i.e., not when it is imported).
   - Code inside this block won't run if the file is being used as an imported module.

### Example:

```python
# sample.py

def greet():
    print("Hello from the function!")

if __name__ == "__main__":
    print("This code is running directly")
    greet()
```

### When You Run the Script Directly:
```bash
$ python sample.py
```
Output:
```
This code is running directly
Hello from the function!
```
- Since the file is run directly, the `if __name__ == "__main__":` block executes.

### When the Script is Imported:
```python
# another_script.py

import sample

sample.greet()
```
Output:
```
Hello from the function!
```
- Here, the message `"This code is running directly"` does not appear because the `if __name__ == "__main__":` block was bypassed when importing the module.

### When to Use It:
1. **For Testing**: If you want to include some test code or example usage within a script but avoid executing it when the script is imported elsewhere, use this construct.
   
2. **Script-Module Duality**: Sometimes, a script is designed to both provide a function (when imported) and work as a standalone program (when executed). The idiom helps separate these behaviors.

### When It Is Not Needed:
1. **Pure Library/Module**: If your script is only intended to be a module for import (and will never be executed directly), you don't need the `if __name__ == "__main__":` block.
   
2. **Top-Level Scripts**: If your script is always going to be executed directly and never imported, the block may not be necessary, although it's still a good practice to use it for flexibility.

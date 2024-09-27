# **Encapsulation, Public, Protected, and Private (Access Modifiers) in Python OOP**

## **1. Introduction to Encapsulation in Python**

### **What is Encapsulation?**
**Encapsulation** is one of the fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, typically a class. Encapsulation also restricts direct access to some of the object's components, which is a way of controlling how the data is modified.

Encapsulation helps:
- **Protect** an object's internal state by preventing external access.
- **Control** modifications to data through specific methods (getters and setters).
- Provide a **clean interface** for interacting with objects, hiding complexity and implementation details.

### **When and Where to Use Encapsulation?**
- When you want to **protect the integrity** of an object’s data by controlling how external code interacts with it.
- When you want to **hide complex implementation details** from the user and provide a simple interface.
- When you want to **restrict direct access** to sensitive data and only allow modification via controlled methods.

---

## **2. Access Modifiers in Python**

In Python, encapsulation is enforced through **access modifiers**. Unlike some other languages (like Java or C++), Python doesn’t have explicit keywords for public, protected, or private access. Instead, it uses naming conventions to control access:

1. **Public**: Accessible from anywhere.
2. **Protected**: Meant to be accessed within the class and subclasses only.
3. **Private**: Only accessible within the class itself.

### **How Access Modifiers Work in Python?**

- **Public**: No special notation. Any method or variable defined normally is public and can be accessed from outside the class.
- **Protected**: Defined with a **single underscore** (`_`) prefix. This suggests that it should not be accessed from outside, but it's still technically accessible.
- **Private**: Defined with **two underscores** (`__`) prefix. This triggers name mangling, making the variable/method hard to access from outside the class.

---

## **3. Example of Encapsulation, Public, Protected, and Private Access**

Here’s a simple example that demonstrates public, protected, and private members in Python.

### **Example: Bank Account Class**

```python
class BankAccount:
    def __init__(self, owner, balance):
        # Public attribute
        self.owner = owner
        
        # Protected attribute
        self._balance = balance
        
        # Private attribute
        self.__account_number = "1234567890"
    
    # Public method to view the balance
    def get_balance(self):
        return self._balance
    
    # Protected method (can be accessed within class or subclass)
    def _deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}")
    
    # Private method (not intended to be accessed directly)
    def __generate_account_report(self):
        return f"Account Report: Owner: {self.owner}, Balance: {self._balance}"
    
    # Public method to get account report (calls the private method)
    def get_account_report(self):
        return self.__generate_account_report()


# Instantiating a BankAccount object
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(f"Account Owner: {account.owner}")

# Accessing protected attribute (though it's discouraged)
print(f"Balance (Protected): {account._balance}")

# Trying to access private attribute (This will fail)
# print(account.__account_number)  # Uncommenting this will raise an AttributeError

# Accessing private attribute through name mangling (not recommended)
print(f"Account Number (Private): {account._BankAccount__account_number}")

# Accessing public method
print(f"Current Balance: {account.get_balance()}")

# Accessing protected method (though it's discouraged)
account._deposit(500)

# Accessing private method via public method
print(account.get_account_report())
```

### **Explanation of the Example:**

1. **Public Members**: 
   - `self.owner`: This attribute is public, meaning it can be accessed directly from outside the class.
   - `get_balance()`: This method is public and can be accessed from anywhere to get the account balance.
   
2. **Protected Members**:
   - `_balance`: This attribute is prefixed with a single underscore, indicating it is **protected**. It can still be accessed directly, but it’s intended to be accessed only within the class or subclass.
   - `_deposit()`: This is a protected method. It can be accessed directly, but by convention, it should only be accessed inside the class or subclass.

3. **Private Members**:
   - `__account_number`: This attribute is private, and Python "name mangles" it to make it difficult to access from outside the class.
   - `__generate_account_report()`: This is a private method that generates an account report. It is only intended to be called within the class.
   
   You can still access private attributes and methods using **name mangling**, as seen with `account._BankAccount__account_number`, but this is generally discouraged.

---
In the provided example, the access modifiers in Python are used to control the visibility and accessibility of the class members (attributes and methods). Python uses **naming conventions** to indicate different levels of access: **public**, **protected**, and **private**. Here’s how they are applied in the example:

### **1. Public Members**
- **Access Modifier**: No underscore (`self.owner`, `get_balance()`, `get_account_report()`)
- **Explanation**: Public members are accessible from anywhere, both inside and outside the class. In the example:
  - The attribute `self.owner` is public, so you can directly access it with `account.owner`.
  - The methods `get_balance()` and `get_account_report()` are public methods that can be called from outside the class.
  
### **2. Protected Members**
- **Access Modifier**: Single underscore prefix (`_self._balance`, `_deposit()`)
- **Explanation**: Protected members are intended to be used within the class or its subclasses. While technically accessible from outside, it’s a convention that external access is discouraged.
  - The attribute `_balance` is protected, meaning it’s intended for internal use but is still accessible directly (`account._balance`).
  - The method `_deposit()` is protected and can be accessed from within the class or subclasses, but it’s not meant to be used by external code.

### **3. Private Members**
- **Access Modifier**: Double underscore prefix (`__self.__account_number`, `__generate_account_report()`)
- **Explanation**: Private members are restricted to the class itself. They are not accessible directly from outside the class, and Python uses **name mangling** to make it difficult to access these members.
  - The attribute `__account_number` is private. You cannot access it directly using `account.__account_number`, but you can access it using name mangling (`account._BankAccount__account_number`), which is generally discouraged.
  - The method `__generate_account_report()` is private, and it can only be accessed within the class. It’s not designed to be called from outside the class directly, although name mangling can technically allow access.

### **Summary of Access Modifiers in the Example:**

| Member                     | Access Modifier | Type       | Access from Outside Class? | Example                             |
|----------------------------|-----------------|------------|----------------------------|-------------------------------------|
| `self.owner`                | Public          | Attribute  | Yes                        | `account.owner`                    |
| `get_balance()`             | Public          | Method     | Yes                        | `account.get_balance()`            |
| `get_account_report()`      | Public          | Method     | Yes                        | `account.get_account_report()`     |
| `_balance`                  | Protected       | Attribute  | Yes (Discouraged)           | `account._balance`                 |
| `_deposit()`                | Protected       | Method     | Yes (Discouraged)           | `account._deposit()`               |
| `__account_number`          | Private         | Attribute  | No (except with name mangling) | `account._BankAccount__account_number` |
| `__generate_account_report()`| Private         | Method     | No (except with name mangling) | `account._BankAccount__generate_account_report()` |



## **4. Why and When to Use Public, Protected, and Private?**

### **Public**:
- Use **public** members when you want to allow full access to certain methods or data.
- Public members define the **interface** that users interact with, and they are usually methods or attributes that are safe to expose.

### **Protected**:
- Use **protected** members when you want to indicate that a member is intended for **internal use** by the class or its subclasses, but you’re not enforcing it strictly.
- This is useful when you expect that subclasses might need to modify certain behavior or access certain attributes without exposing them to the outside world.

### **Private**:
- Use **private** members when you want to strictly **limit access** to certain attributes or methods, ensuring that no external code or subclass can modify them directly.
- Private members are useful for sensitive data or critical methods that should not be modified or accessed from outside the class. It helps in **enforcing encapsulation**.

---

## **5. Real-World Use Case of Encapsulation**

Consider a **banking system** where:
- You have a bank account with a **balance** (protected) and an **account number** (private).
- You don’t want external code to directly modify the balance or account number. Instead, you provide public methods like `deposit()` or `withdraw()` to control the balance in a safe way.
- You also want to hide sensitive details like the account number, and only provide limited access through public methods like `get_account_report()`.

Encapsulation allows the system to **hide the internal details** while providing **controlled access** to sensitive data.

---

## **6. Key Takeaways**

- **Encapsulation** allows you to bundle data and methods in a class while controlling access to the internal state.
- **Public members** are fully accessible from outside the class. These define the class's external interface.
- **Protected members** (prefixed with `_`) are intended for use within the class and its subclasses, though they can still be accessed externally.
- **Private members** (prefixed with `__`) are strictly meant to be accessed only within the class, and Python uses name mangling to prevent direct access.
- Use **public** members for methods and data that should be accessible, **protected** for members that are for internal or subclass use, and **private** for sensitive or critical data that shouldn’t be accessed or modified directly.

---

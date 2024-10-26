"""Module for Arithematic Calculations"""


def multiply(a: int, b: int) -> int:
    return a*b


def add(a: int, b: int) -> int:
    return a+b


def divide(a: int, b: int) -> float:
    return a/b


def subtract(a: int, b: int) -> int:
    return a-b

def very_long_function_name_hard ():
    pass


if __name__ == "__main__":
    
    first_number = int(input("Enter first number "))
    second_number = int(input("Enter second number "))

    print(add(first_number,second_number))

    print(subtract(10,9))
    print(__name__)
    print("Hello i am in calculations.py file")
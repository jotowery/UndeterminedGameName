print(24 + 34 / 100 - 1023)

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Now we'll do the math problem with just functions")

addition_part = add(24, 34)
subtraction_part = subtract(100, 1023)
division_part = divide(addition_part, subtraction_part)

print(f"The answer is", division_part)

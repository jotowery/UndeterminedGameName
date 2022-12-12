
def add(a, b):
    print("ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print("SUBTRACTING {a} - {b}")
    return a - b

def divide(a, b):
    print("DIVIDING {a} / {b}")
    return a / b

print("Give me a value for 'a':")
input1 = float(input("> "))
print("Give me a value for 'b':")
input2 = float(input("> "))
print("Lastly, give me one more value for 'c':")
input3 = float(input("> "))

print("I want to divide c by a.")
print(f"{input3} / {input1}")
divide(input3, input1)

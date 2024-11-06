#PRACTICAL 15
'''Write a python program to Illustrate all operators in python.'''
def arithmetic_operators(a, b):
    print("Arithmetic Operators")
    print(f"{a} + {b} = {a + b}")    # Addition
    print(f"{a} - {b} = {a - b}")    # Subtraction
    print(f"{a} * {b} = {a * b}")    # Multiplication
    print(f"{a} / {b} = {a / b}")    # Division
    print(f"{a} % {b} = {a % b}")    # Modulus
    print(f"{a} ** {b} = {a ** b}")  # Exponentiation
    print(f"{a} // {b} = {a // b}")  # Floor Division
    print()
arithmetic_operators(10,2)

def comparison_operators(a, b):
    print("Comparison Operators")
    print(f"{a} == {b} = {a == b}")  # Equal
    print(f"{a} != {b} = {a != b}")  # Not equal
    print(f"{a} > {b} = {a > b}")    # Greater than
    print(f"{a} < {b} = {a < b}")    # Less than
    print(f"{a} >= {b} = {a >= b}")  # Greater than or equal to
    print(f"{a} <= {b} = {a <= b}")  # Less than or equal to
    print()
comparison_operators(10,2)

def logical_operators(a, b):
    print("Logical Operators")
    print(f"{a} and {b} = {a and b}")  # and
    print(f"{a} or {b} = {a or b}")    # or
    print(f"not {a} = {not a}")        # not
    print()
logical_operators(10,2)

def bitwise_operators(a, b):
    print("Bitwise Operators")
    print(f"{a} & {b} = {a & b}")  # AND
    print(f"{a} | {b} = {a | b}")  # OR
    print(f"{a} ^ {b} = {a ^ b}")  # XOR
    print(f"~{a} = {~a}")          # NOT
    print(f"{a} << 1 = {a << 1}")  # Zero fill left shift
    print(f"{a} >> 1 = {a >> 1}")  # Signed right shift
    print()
bitwise_operators(10,2)

def assignment_operators():
    print("Assignment Operators")
    a = 10
    print(f"a = {a}")
    a += 5
    print(f"a += 5 -> {a}")
    a -= 3
    print(f"a -= 3 -> {a}")
    a *= 2
    print(f"a *= 2 -> {a}")
    a /= 4
    print(f"a /= 4 -> {a}")
    a %= 3
    print(f"a %= 3 -> {a}")
    a **= 2
    print(f"a **= 2 -> {a}")
    a //= 2
    print(f"a //= 2 -> {a}")
    print()
assignment_operators()
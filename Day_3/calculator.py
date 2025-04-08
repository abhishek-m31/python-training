def add(*args):
    return sum(args)

def subtract(n1, n2):
    return n1 - n2

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

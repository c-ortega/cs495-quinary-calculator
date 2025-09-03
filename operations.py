def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    if num2 == 0:
        result = "Error"
    else:
        result = num1 // num2
    return result

def square(num):
    result = num * num
    return result

def square_root(num):
    if num < 0:
        result = "Error"
    else:
        result = int(num ** 0.5)
    return result
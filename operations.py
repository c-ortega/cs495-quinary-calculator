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
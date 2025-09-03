import operations

def quinaryCalculator():

#   base 5. We take in the input as base 5 quinary
    numInput1 = "13"
    numInput2 = "3"

#   base 10 integers. Convert the base 5 into decimal base 10
    numInput1Decimal = int(numInput1, 5)
    numInput2Decimal = int(numInput2, 5)

    add = operations.addition(numInput1Decimal, numInput2Decimal);
    sub = operations.subtraction(numInput1Decimal, numInput2Decimal);
    multiply = operations.multiplication(numInput1Decimal, numInput2Decimal);
    divide = operations.division(numInput1Decimal, numInput2Decimal);

    print(f"(Base 10) num1 + num2 = {add}")
    # print(f"(Base 10) num1 - num2 = {sub}")
    # print(f"(Base 10) num1 * num2 = {multiply}")
    # print(f"(Base 10) num1 // num2 = {divide}")

    result = add
    # result = sub
    # result = multiply
    # result = divide

#   back to base 5. Get remainder from result and add to string. Then, do floor division for next digit. Loop through each decimal place.
    quinary = ""
    if type(result) == str:
        return print(result)
    else:
        while result > 0:
            remainder = result % 5
            quinary = str(remainder) + quinary
            result //= 5
        return print(f"Converted result to base 5 = {quinary}")

if __name__ == "__main__":
    quinaryCalculator()
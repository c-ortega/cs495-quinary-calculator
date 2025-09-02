def quinaryCalculator():

#   base 5. We take in the input as base 5 quinary
    numInput1 = "13"
    numInput2 = "3"

#   base 10 integers. Convert the base 5 into decimal base 10
    numInput1Decimal = int(numInput1, 5)
    numInput2Decimal = int(numInput2, 5)
    result = numInput1Decimal + numInput2Decimal
    print(result)

#   back to base 5. Get remainder from result and add to string. Then, do floor division for next digit. Loop through each decimal place.
    quinary = ""
    while result > 0:
        remainder = result % 5
        quinary = str(remainder) + quinary
        result //= 5
    return print(quinary)

if __name__ == "__main__":
    quinaryCalculator()
import operations
import math

class Calc:
    def __init__(self):
        self.clear()

    def clear(self):
        self.current_input = ""
        self.previous_value = None
        self.operation = None

    def push_digit(self, digit):
        if digit not in "01234":
            raise ValueError("Only digits 0-4 are valid in base 5")
        self.current_input += digit

    def set_operation(self, op):
        if op not in {"+", "-", "*", "/", "sq", "sqrt"}:
            raise ValueError(f"Unsupported operation: {op}")
        
        if op in {"sq", "sqrt"}:
            self.previous_value = int(self.current_input, 5)
            self.operation = op
            self.equal()  # immediately compute
        else:
            if self.current_input == "":
                raise ValueError("No input")
            self.previous_value = int(self.current_input, 5)
            self.current_input = ""
            self.operation = op

    def equal(self):
        if self.operation is None:
            return
        
        if self.operation in {"sq", "sqrt"}:
            operand = self.previous_value
        else:
            if self.current_input == "":
                raise ValueError("Missing second operand")
            operand = int(self.current_input, 5)

        if self.operation == "+":
            result = operations.addition(self.previous_value, operand)
        elif self.operation == "-":
            result = operations.subtraction(self.previous_value, operand)
        elif self.operation == "*":
            result = operations.multiplication(self.previous_value, operand)
        elif self.operation == "/":
            result = operations.division(self.previous_value, operand)
            if isinstance(result, str):  # Error from division
                self.current_input = ""
                self.previous_value = None
                self.operation = None
                raise ValueError(result)
        elif self.operation == "sq":
            result = operations.square(self.previous_value)
        elif self.operation == "sqrt":
            result = operations.square_root(self.previous_value)
        else:
            raise ValueError("Invalid operation")

        self.current_input = self._to_quinary(result)
        self.previous_value = None
        self.operation = None

    def get_display_quinary(self):
        return self.current_input or "0"

    def get_display_decimal(self):
        try:
            return str(int(self.current_input, 5))
        except:
            return "Error"

    def _to_quinary(self, num):
        if num == 0:
            return "0"
        quinary = ""
        while num > 0:
            quinary = str(num % 5) + quinary
            num //= 5
        return quinary
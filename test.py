class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        return Calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        return Calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        return Calculator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ValueError("Division by zero is not allowed.")
            return Calculator(self.value / other.value)
        if other == 0:
            raise ValueError("Division by zero is not allowed.")
        return Calculator(self.value / other)

    def __repr__(self):
        return f"Calculator({self.value})"
a = Calculator(10)
b = Calculator(5)



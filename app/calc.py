import app
import math

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
        
    def square(self, x):
        self.check_type(x)
        if x < 0:
            raise TypeError("The square of a negative is not possible")
        return math.sqrt(x)
        
    def logarithm(self, x):
        self.check_type(x)
        if x <= 0:
            raise TypeError("The logarithm of a negative or zero is not possible")
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
            
    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameters must be numbers")



if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)

from math import sqrt

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def square(self):
        return Complex(self.real ** 2 - self.imaginary ** 2, 2 * self.real * self.imaginary)

    def __repr__(self) -> str:
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    def magnitude(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)


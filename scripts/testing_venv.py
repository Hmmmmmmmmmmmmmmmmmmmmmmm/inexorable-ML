class Complex_Number_Ops:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex_Number_Ops(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex_Number_Ops(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        real = (self.x * other.x) - (self.y * other.y)
        imag = (self.y * other.x) + (self.x * other.y)
        return Complex_Number_Ops(real, imag)

    def __truediv__(self, other):
        deno = other.x ** 2 + other.y ** 2
        real = ((self.x * other.x) + (self.y * other.y)) / deno
        imag = ((self.y * other.x) - (self.x * other.y)) / deno
        return Complex_Number_Ops(real, imag)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}) + i({self.y})"

if __name__ == "__main__":
    a = Complex_Number_Ops(3, 2)
    b = Complex_Number_Ops(1, 7)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a == b?", a == b)

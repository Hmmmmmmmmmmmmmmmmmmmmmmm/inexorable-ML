# from app import *
from app import add, sub, mul, div
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
except ValueError:
    print("Please enter valid integers!")
    exit()

result1 = add(a,b)
result2 = sub(a,b)
result3 = mul(a,b)
result4 = div(a,b)


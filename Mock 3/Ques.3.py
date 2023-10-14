import math

num1 = int(input())
num2 = int(input())

gcd = math.gcd(num1, num2)

if gcd == 1:
    print("Coprime")
else:
    print("Not Coprime")
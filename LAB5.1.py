import math

x = float(input("Введіть число: "))

if x >= 6:
    x = 3 ** (x-4) + math.log( math.e, x ) + math.log10(x)
    print(f"\nВідповідь: X = {round(x,2)}!")
elif -1<x and x < 6:
    x = x ** 2 + math.sin(2*x)
    print(f"\nВідповідь: X = {round(x,2)}!")
else:
    x = 2 + 2.7 * (x ** 2)
    print(f"\nВідповідь: X = {round(x, 2)}!")
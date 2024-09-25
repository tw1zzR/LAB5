import  math

# Діаметр та радіус кулі
d = float(input("Введіть діаметр кулі: "))
r = d/2

# Точки в просторі
x = float(input("\nВведіть координату x: "))
y = float(input("Введіть координату y: "))
z = float(input("Введіть координату z: "))

a = (x,y,z)

# Головний код
distance = math.sqrt(x**2+y**2+z**2)

if distance <= r:
    print(f"\nВаша точка A{a} належить кулі з діаметром d={d}!")
else:
    print(f"\nВаша точка A{a} не належить кулі з діаметром d={d}!")

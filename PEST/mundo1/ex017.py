from math import sqrt
op = float(input('digite o cateto oposto: '))
ad = float(input('digite o cateto adjacente: '))

hip = op**2 + ad**2

print(f'a hipotenusa do triangulo é {sqrt(hip):.2f}')
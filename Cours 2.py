a, b, c = 2, 3, 4
print("A = {}, B = {}, C = {}.".format(a, b, c))

a = float(input("Entrez A : "))
b = float(input("Entrez B : "))
print("Le résultat est {} ! ".format(a*b))

from math import pi
def v(r, h):
  return (1/3) * pi * r**2 * h
print(int(v(10, 3)))
print(int(v(10, 5)))
print(int(v(15, 2)))
print(int(v(12, 5)))

temp = float(input("Entrez une température en °C : "))
print("{} °C donne {} K !".format(temp, temp + 273.15))

c = float(input("Entrez la longueur d'un côté > "))
print("Le cube a une surface de {} cm^2 et un volume de {} cm^3".format(c**2, c**3))

t10 = int(input("Entrez le nombre de tickets de 10€ que vous avez > "))
t20 = int(input("Entrez le nombre de tickets de 20€ que vous avez > "))
t50 = int(input("Entrez le nombre de tickets de 50€ que vous avez > "))
print("Vous avez {}€ au total !".format(t10 * 10 + t20 * 20 + t50 * 50))

r = float(input("Entrez le rayon du cercle (en cm) > "))
print("Le cercle a un périmètre de {} cm et une aire de {} cm !".format(round(2*pi*r, 2), round(pi*r**2, 2)))

r = float(input("Entrez le rayon de la sphere (en cm) > "))
print("La sphere a une surface de {} cm et un volume de {} cm !".format(round(4*pi*r**2, 2), round((4/3)*pi*r**3, 2)))

from math import exp
A = float(input("Entrez A (en s^-1) > "))
E = float(input("Entrez E (en kJ.mol^-1) > "))
T = float(input("Entrez la température (en °C) > ")) + 273.15
R = 8.3144621
print(A * exp(-E/(R*T)))

from math import sqrt, cos, radians
a = float(input("Entrez la longueur du premier côté (en cm) > "))
b = float(input("Entrez la longueur du deuxième côté (en cm) > "))
c = radians(int(input("Entrez l'angle entre les deux côtés (en °) > ")))
print("Le troisième côté a une longueur de {} cm !".format(round(sqrt(a**2 + b**2 - 2 * a * b * cos(c)), 2)))
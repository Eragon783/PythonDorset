print(len("Hello World !"))

print(("Hello World !")[6])

print(("Hello World !")[2:8])

print(("Hello World !")[:8])
print(("Hello World !")[3:])

print(("Hello World !")[-3])
print(("Hello World !")[0:-3])

print(("Hello World !").count("o"))
print(("Hello World !").find("o"))

print(("Hello World !").lower())
print(("Hello World !").upper())

print(("Hello World !").replace("Hello", "ABCDE"))

if (int(input("Entrez un entier > ")) < 8):
    print("Yesss")
else:
    print("Nooo")
    
poids = float(input("Entrez votre poids (en kg) > ")) / (float(input("Entrez votre taille (en m) > ")))**2
if poids < 18.5:
    print("Underweight")
elif poids < 25:
    print("Normal weight")
elif poids < 30:
    print("Overweight")
else:
    print("Obesity")
    
poids = input("Entrez votre taille (en m ou cm) > ")
if poids[-2:] == "cm":
    poids = float(poids[:-2])/100
elif poids[-1] == "m":
    poids = float(poids[0:-1])
print(poids)

num1 = int(input("Entrez un entier > "))
num2 = int(input("Entrez un autre entier > "))
if (num1 % num2 == 0):
    print("{} est divisible par {} et le quotient vaut {}.".format(num1, num2, num1//num2))
else:
    print("{} n'est pas divisible par {}, le quotient des deux vaut {} et le reste {}".format(num1, num2, num1//num2, num1%num2))
    
num1 = float(input("Entrez un nombre > "))
num2 = float(input("Entrez un autre nombre > "))
num3 = float(input("Entrez un autre nombre > "))
print("Le plus petit nombre est {}".format(min(num1, num2, num3)))

unité = int(input("Entrez votre nombre d'unité > "))
print("La facture sera de {} € !".format(min(max(0, unité - 100), 100) * 5 + max(0, unité - 200) * 10))
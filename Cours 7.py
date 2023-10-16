n = "a"
liste = []
while n != "":
    n = input("Entrez un entier > ")
    if n != "":
        liste.append(int(n))
print("La moyenne vaut : {}".format(sum(liste)/len(liste)))

n = input("Entrez la liste des noms (séparés par un espace) > ").split(" ")
for i in n:
    print("Hi {} !".format(i))
    
element = ["H", "C", "N", "O", "S", "Cl"]
masseatomique = [1.008, 12.011, 14.007, 15.999, 32.065, 35.453]
masse = 0
for i in range(len(element)):
    masse += masseatomique[i] * int(input("Combien de {} dans votre element ? ".format(element[i])))
print("La masse totale est de {}".format(masse))

n = int(input("Entrez le degré de votre polynome > "))
coefficients = []
for i in range(n):
    coefficients.append(int(input("Entrez le coefficient de x^{} > ".format(i))))
x = int(input("Pour quelle valeur de x doit on calculer f(x) > "))
f = 0
for i in range(len(coefficients)):
    f += coefficients[i] * x**i
print("f({}) = {}".format(x, f))


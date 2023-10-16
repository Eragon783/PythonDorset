def fct (**kid):
    print("Son nom de famille est " + kid["nomdefamille"])
    
fct(prénom = "Michel", nomdefamille = "Berger")

def fct2(*nombres):
    print("Le deuxième nombre est {}".format(nombres[1]))
    
fct2(1, 2)

def max2(a, b):
    return max(a, b)

print(max2(2, 3))

def fct3():
    liste = []
    for i in range(5):
        liste.append(int(input("Entrez le {}e nombre > ".format(i + 1))))
    print("La liste crée est {}".format(liste))
    print("Le maximum de la liste est {} et le minimum est {} !".format(min(liste), max(liste)))
    
fct3()

def fct4():
    try:
        n = int(input("Entrez un nombre > "))
        if n < 1:
            raise Exception()
        if (n % 2 == 0):
            print("{} est pair !".format(n))
        else:
            print("{} est impair !".format(n))
    except:
        print("Entrez un nombre valide !")
        fct4()
        
fct4()


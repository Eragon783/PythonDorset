elements = {
    "H" : {
        "Element" : "Hydrogen",
        "Atomic number" : 1,
        "Melting point" : 14,
        "Boiling point" : 20
    },
    "He" : {
        "Element" : "Helium",
        "Atomic number" : 2,
        "Melting point" : 1,
        "Boiling point" : 4
    },
    "Li" : {
        "Element" : "Lithium",
        "Atomic number" : 3,
        "Melting point" : 453,
        "Boiling point" : 1603
    },
    "Be" : {
        "Element" : "Beryllium",
        "Atomic number" : 4,
        "Melting point" : 1560,
        "Boiling point" : 2742
    },
    "B" : {
        "Element" : "Boron",
        "Atomic number" : 5,
        "Melting point" : 2349,
        "Boiling point" : 4200
    },
    "C" : {
        "Element" : "Carbon",
        "Atomic number" : 6,
        "Melting point" : 3915,
        "Boiling point" : 3915
    },
    "N" : {
        "Element" : "Nitrogen",
        "Atomic number" : 7,
        "Melting point" : 63,
        "Boiling point" : 77
    },
    "O" : {
        "Element" : "Oxygen",
        "Atomic number" : 8,
        "Melting point" : 54,
        "Boiling point" : 90
    },
    "F" : {
        "Element" : "Fluorine",
        "Atomic number" : 9,
        "Melting point" : 53,
        "Boiling point" : 85
    },
    "Ne" : {
        "Element" : "Neon",
        "Atomic number" : 10,
        "Melting point" : 25,
        "Boiling point" : 27
    }
}

def F():
    element = input("Entrez le symbole d'un élément > ")
    if (element in elements):
        température = int(input("Entrez la température de votre élément > "))
        température_liquide = elements[element]["Melting point"]
        température_gaz = elements[element]["Boiling point"]
        if température < température_liquide: 
            print("L'élément est solide")
        elif température < température_gaz: 
            print("L'élément est liquide")
        else:
            print("L'élément est gazeux")
    else:
        print("Le symbole entré n'est pas répertorié !")
        
F()

banques = {
    "ANZ" : {
        "années 1 et 2" : 2.3,
        "années 3 et plus" : 4.1
    },
    "Bank of Australia" : {
        "années 1 et 2" : 0.1,
        "années 3 et plus" : 5
    },
    "Commonwealth Bank" : {
        "années 1 et 2" : 3.5,
        "années 3 et plus" : 3.8
    },
    "Westpac" : {
        "années 1 et 2" : 3.7,
        "années 3 et plus" : 3.7
    }
}

def G():
    banque = input("Entrez le nom de votre banque > ")
    if (banque in banques):
        durée = int(input("Entrez la durée du prêt (en mois) > "))
        montant = int(input("Entrez le montant du prêt > "))
        interets = banques[banque]["années 1 et 2"]/(100 * 12) * montant * min(24, durée) + banques[banque]["années 3 et plus"]/(100 * 12) * montant * max(0, durée - 24)
        print("Les interêts totaux valent {}".format(round(interets, 2)))
    else:
        print("La banque entrée n'est pas répertorié !")
        
G()
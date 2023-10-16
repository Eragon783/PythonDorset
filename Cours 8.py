capitals = {
    "France" : "Paris",
    "Italie" : "Rome",
    "Irlande" : "Dublin"
}

capitals = dict([("France", "Paris"),("Italie", "Rome"), ("Irlande", "Dublin")])

print(capitals)
print(len(capitals))

dictionnaire = {
    1 : "un",
    2 : "deux",
    3 : {
            5 : "trente cinqt",
            6 : "trente six"
        }
}
print(dictionnaire[3][6])

dictionnaire[4] = "quatre"
print(dictionnaire)

del dictionnaire[4]
print(dictionnaire)

villes = ("Paris", "Athens", "Madrid")
continent = "Europe"
dictionnaire = dict.fromkeys(villes, continent)
print(dictionnaire)

villes = ("Paris", "Athens", "Madrid")
pays = ["France", "Grèce", "Espagne"]
dictionnaire = dict.fromkeys(villes, pays)
print(dictionnaire)

keys = ["Dix", "Vingt", "Trente"]
values = [10, 20, 30]
dictionnaire = dict(zip(keys, values))
print(dictionnaire)

dict1 = {'Dix': 10, 'Vingt': 20, 'Trente': 30}
dict2 = {'Quarante': 40, 'Cinquante': 50, 'Soixante': 60}
dict1.update(dict2)
print(dict1)

dict = {
    "class" : {
        "student" : {
            "name" : "Mike",
            "marks" : {
                "physics" : 70,
                "history" : 80
            }
        }
    }
}
print(dict["class"]["student"]["marks"]["history"])

dictionnaire = {
    "name" : "Kelly",
    "age" : 25,
    "salary" : 8000,
    "city" : "New York"
}
keys = ["name", "salary"]
for key in keys:
    dictionnaire.pop(key)
print(dictionnaire)

dictionnaire = {
    "a" : 100,
    "b" : 200,
    "c" : 300
}
print(200 in dictionnaire.values())

dictionnaire = {
    "emp1" : {
        "name" : "John",
        "salary" : 7500
    },
    "emp2" : {
        "name" : "Emma",
        "salary" : 8000
    },
    "emp3" : {
        "name" : "Brad",
        "salary" : 500
    }
}
dictionnaire["emp3"]["salary"] = 8500
print(dictionnaire)
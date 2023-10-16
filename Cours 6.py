Liste = ["Nicolas", "Teanie", "Mathias", "Tara", "Cléa"]
print(Liste)

for Element in Liste:
    print(Element)
    
print(Liste[0:2])

Liste.append("A")
print(Liste)

Liste.remove("A")
print(Liste)

#Liste [ ... , ... ] -> mutable
#Tuple ( ... , ... ) -> immutable

tuple = ("Nicolas", "Teanie", "Mathias", "Tara", "Cléa")

#Set { ... , ... } -> non ordonné et ne peux pas contenir de doublons

set = {"Nicolas", "Teanie", "Mathias", "Tara", "Cléa"}

print(Liste[:2])
print(Liste[2:])

Liste2 = [3.14, 7, -2 + 3j, "water", False, [1, 2], 5, "Hello", "Hi", "7", "e"]
print(Liste2[::3])
print(Liste2[-1])

ElementSupprimé = Liste2.pop();
print(ElementSupprimé)
print(Liste2)

n = int(input("Entrez un entier > "))
liste = []
for i in range(n):
    liste.append(1/(i+1))
print("La somme vaut {} !".format(round(sum(liste), 2)))

string = "1,2,3"
print(string.split(","))

n = int(input("Entrez un entier > "))
liste = []
for i in range(n+1):
    liste.append(str(i**2))
print("La liste des carrés de ces entiers est : {}.".format(", ".join(liste)))

noms = []
notes = []
string = "a"
while string != "":
    string = str(input("Entrez un nom > "))
    if string != "": 
        noms.append(string)
        notes.append(int(input("Entrez sa note > ")))
print("La moyenne des élèves est {}".format(sum(notes)/len(notes)))
for i in range(len(noms)):
    print(noms[i] + " : " + str(notes[i]))
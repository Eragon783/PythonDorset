num = int(input("Entrez une valeur entière > "))
while num > 0:
    print("Le division enti�re de {} par 3 donne {} !".format(num, num//3))
    num = int(input("Entrez une valeur entière > "))
print("Terminé")

num = int(input("Entrez une valeur entière > "))
ndiv = 1
while ndiv < num:
    print("Le division enti�re de {} par {} donne {} !".format(num, ndiv, num//ndiv))
    ndiv += 1
print("Terminé")

num = int(input("Entrez une valeur entière > "))
ndiv = 0
while num > 0:
    print("Le resultat de la division de {} par 3 donne {}".format(num, num//3))
    ndiv += 1
    print("Nombre de division : {}".format(ndiv))
    num = int(input("Entrez une valeur entière > "))
    
i = 1
c = 0
while i <= 211:
    if i%3 == 0:
        c += 1
    i += 1
print("Le nombre de chiffre divisibles par 3 entre 0 et 211 est : {} !".format(c))

i = 0
c = 0 
while i <= 10:
    c += i
    i += 1
print("La somme des 10 premiers nombres naturels vaut {} !".format(c))

i = 1
s = 0
while i <= 10:
    s += int(input("Entrez un entier > "))
    i += 1
print("La moyenne des 10 nombres entrés vaut {} !".format(s/10))


i = 1
while i < 20:
    print("*"*i)
    i += 1
    
num = int(input("Entrez une valeur entière > "))
if num < 0:
    print("Entrez une valeur positive !")
else:
    fact = 1
    save = num
    if num != 0:
        while num > 1:
            fact *= num
            num -= 1
    print("Le factoriel de {} est {} !".format(save, fact))
    
name="Jesaa29Roy"
size = len(name)
i = 0
while i < size:
    if name[i].isdecimal():
        break
    print(name[i], end='')
    i += 1
print("\nTerminé")

name="Jesaa29Roy"
size = len(name)
i = -1
while i < size - 1:
    i += 1
    if not name[i].isalpha():
        continue
    print(name[i], end='')
print("\nTerminé")

num = int(input("Entrez une valeur entière > "))
for i in range (num+1):
    print("Le carré de {} est {} !".format(i, i**2))
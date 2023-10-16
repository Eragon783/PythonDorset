n = int(input("Entrez un entier > "))
m = int(input("Entrez un pas > "))
for i in range(2,n,m):
    print(i**2)
    
sum = 0
for i in range(10):
    sum += i
    print("Le résultat de la somme est {}".format(sum))
    
prod = 1
for i in range(1,10):
    prod *= i
    print("Le résultat du produit est {}".format(prod))
    
for i in range(3):
    for j in range(3):
        print("i = {}, j = {}".format(i, j))
        
n = int(input("Entrez un entier > "))
sum = 0
for i in range(n + 1):
    sum += i
print("La somme des {} premiers entiers vaut {}".format(n, sum))

n = int(input("Entrez un entier > "))
sum = 0
for i in range(1, n + 1):
    sum += (i+1)/i**2
print("Le résultat de la somme est {: .2f} !".format(sum))

n = int(input("Entrez un entier > "))
produit = 1
for i in range(1, n + 1):
    produit *= i
print("Le factoriel de {} est {} !".format(n, produit))

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}{j}")
        
for i in range(1, 10):
    for j in range(1,10):
        if i != j:
            print(f"{i}{j}")
            
n = int(input("Entrez le nombre de ligne de votre triangle > "))
print("Votre tiangle a {} valeur(s) !".format(int(n * (n + 1)/2)))

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            print("{}{}{}".format(i, j, k))
            
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i+j+k == 22:
                print(f"{i}{j}{k}")
             
print("Les nombres qui sont égaux à la somme des cubes de leurs chiffres sont : ", end="")
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            n = int(str(i) + str(j) + str(k))
            if i**3+j**3+k**3 == n:
                print(n, end=" ")
                
                
n = int(input("Entrez un entier > "))
for i in range(1, n + 1):
    if n%i == 0:
        print(i)
        
n = int(input("Entrez un entier > "))
sum = 0
print("La liste des {} premiers nombres entiers est : ".format(n), end="")
for i in range(0, n):
    m = 2*i + 1
    sum += m
    print(m, end=" ")
print("\nLa somme de tous ces nombres vaut {} !".format(m))

n = int(input("Entrez un nombre entier > "))
premier = True
for i in range(2, int(n/2 + 1)):
    if n%i == 0:
        premier = False
print("{} est-il premier ? {}".format(n, premier))

a = 0
b = 1
n = int(input("Entrez le nombre de termes de la suite de Fibonacci que vous voulez calculer > "))
string = "0, "
for i in range(n):
    c = b
    b = a
    a = a + c 
    string += str(a)
    if i != n-1: string += ", "
print("Les {} premiers termes de la suite de Fibonacci sont : {}".format(n, string))

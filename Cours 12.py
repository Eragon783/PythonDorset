import matplotlib.pyplot as plt
import numpy as np
import math as m

x = np.linspace(-2, 2, 101)
y = x ** 2
plt.plot(x, y)
plt.show()

x = np.linspace(0, 3 * np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title("A simple chirp")
plt.show()

x = np.linspace(-2, 2, 101)
y = x ** 2
plt.plot(y)
plt.show()

x = np.linspace(-2, 2, 101)
y = x ** 2
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.5, 2.5)
plt.title("Chart title")
plt.plot(x, y)
plt.show()

x = np.linspace(-2, 2, 101)
y = x ** 2
plt.plot(x, y, label="x ** 2")
y = x
plt.plot(x, y, label="x")
plt.legend()
plt.show()

plt.savefig("fig.png")

x = np.linspace(-1, 1, int(input("Combien de points voulez-vous afficher ? ")))
y = np.cos(2 * np.pi * x)
plt.xlabel("x")
plt.ylabel("y = cos(2 * pi * x)")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.title("Body function(2 * pi * x)")
plt.plot(x, y)
plt.show()
plt.savefig("cos2pix.png")

x = np.linspace(-1, 1, int(input("Combien de points voulez-vous afficher ? ")))
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "b", label="cos")
y = np.sin(2 * np.pi * x)
plt.plot(x, y, "r", label="sin")
plt.xlabel("x")
plt.ylabel("y = cos(2 * pi * x)")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.title("Body function(2 * pi * x)")
plt.legend()
plt.show()

x = np.linspace(0, 4, int(input("Combien de points voulez-vous afficher ? ")))
y = np.sin(np.pi * x) * np.sin(20 * np.pi * x) * np.exp(-x)
plt.plot(x, y, "b")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 4)
plt.title("Graph")
plt.show()

temp = int(input("Quelle est la température du gaz ? "))
x = np.linspace(2, 10, int(input("Combien de points voulez-vous afficher ? ")))
y = 0.008206 * temp/x
plt.plot(x, y)
plt.xlabel("V (L)")
plt.ylabel("P (hPa)")
plt.title("Isotherm (ideal gas)")
plt.show()
plt.savefig("isotherm.png")

n = int(input("Quel est le nombre de température ? "))
a = int(input("Combien de points voulez-vous afficher ? "))
for i in range(n):
    temp = int(input("Quelle est la température du gaz ? "))
    x = np.linspace(2, 10, a)
    y = 0.008206 * temp/x
    plt.plot(x, y)
plt.xlabel("V (L)")
plt.ylabel("P (hPa)")
plt.title("Isotherm (ideal gas)")
plt.show()
plt.savefig("isotherm.png")

x0 = float(input("Quelle est la valeur de x0 ? "))
s = float(input("Quelle est la valeur de s ? "))
xstart = int(input("Quelle est la première valeur de l'intervalle ? "))
xend = int(input("Quelle est la dernière valeur de l'intervalle ? "))
n = int(input("Quelle est le nombre de points à afficher ? "))

x = np.linspace(xstart, xend, n)
y = 1/m.sqrt(2 * np.pi) * np.exp(-1/2 * (x - x0) ** 2/s ** 2)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(xstart, xend)
plt.title("Gaussian fonction")
plt.show()

x = np.linspace(0, 3, 100)
y = np.exp(-x)
plt.plot(x, y, label="exp(-x)")
y = np.sin(3 * np.pi * x) * np.exp(-x)
plt.plot(x, y, label="sin(3 * pi * x) * exp(-x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(0, 3)
plt.ylim(-0.6, 1)
plt.title("Fonctions")
plt.legend()
plt.show()

c = int(input("Quelle est le nombre de courbes de Gauss à afficher ? "))
xstart = int(input("Quelle est la première valeur de l'intervalle ? "))
xend = int(input("Quelle est la dernière valeur de l'intervalle ? "))
n = int(input("Quelle est le nombre de points à afficher ? "))
x = np.linspace(xstart, xend, n)

for i in range(c):
    x0 = float(input("Quelle est la valeur de x0 ? "))
    s = float(input("Quelle est la valeur de s ? "))
    y = 1/m.sqrt(2 * np.pi) * np.exp(-1/2 * (x - x0) ** 2/s ** 2)
    plt.plot(x, y, label=f"x0 = {x0} et s = {s}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(xstart, xend)
plt.title("Gaussian fonction")
plt.show()
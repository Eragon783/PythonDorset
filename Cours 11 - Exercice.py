import numpy as np
import math as m
import statistics as st

#Exercice 1
vector = np.linspace(1.0, 5.0, 21)
print("Values in Angstroms : {}".format(vector))
for i in range(len(vector)):
    vector[i] = vector[i] * 0.1
print("Values in Nanometers : {}".format(vector))

#Exercice 2
start = float(input("Enter the starting value > "))
end = float(input("Enter the ending value > "))
length = int(input("Enter the number of values > "))

x0 = float(input("Enter x0 > "))
s = float(input("Enter s > "))

x = np.linspace(start, end, length)
y = np.zeros(length)

print("   x      y")
for i in range(len(y)):
    y[i] = 1/m.sqrt(2 * m.pi) * m.exp(-1/2 * ((x[i] - x0)**2/s**2))
    print("{}   {}".format(format(round(x[i], 3), '.3f'), format(round(y[i], 5)), '.3f'))

#Exercice 3
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']

t = np.array(temp_mar)
m = np.array(months)

print("The mean temperature is {}".format(round(st.mean(t), 1)))

index_min=temp_mar.index(min(temp_mar))
index_max=temp_mar.index(max(temp_mar))
print("The coldest month is {} with {} °C".format(m[index_min], t[index_min]))
print("The warmest month is {} with {} °C".format(m[index_max], t[index_max]))

#Exercice 4
length = int(input("Enter the number of student > "))
theory = np.zeros(length)
problem = np.zeros(length)
total = np.zeros(length)

for i in range(length):
    theory[i] = float(input("Enter the grade in theory of the {}e student (from 0 to 10) > ".format(i + 1)))
    problem[i] = float(input("Enter the grade in problem of the {}e student (from 0 to 10) > ".format(i + 1)))
    total[i] = theory[i] * 0.4 + problem[i] * 0.6

print("Index | Theory | Problem | Total")
for i in range(length):
    print("Student {} | {} | {} | {}".format(i, theory[i], problem[i], total[i]))

print("The maximum total grade is {}".format(max(total)))
print("The minimum total grade is {}".format(min(total)))
print("The mean total grade is {}".format(np.mean(total)))
print("The maximum total grade is on the index {}".format(np.where(total == max(total))[0][0]))
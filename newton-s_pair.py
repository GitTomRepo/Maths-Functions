# PYTHON_3
# Author : GitTomRepo
# Link :

from math import *
a = float(input("a = "))
b = float(input("b = "))
n = int(input("n = "))
nb = float(0)
for i in range (0, n+1) :
    combinaison = (factorial(n) / (factorial(i) * factorial(n - i)))
    nb = nb + (combinaison) * (a**(n-i)) * (b**i)
print("Nombre : ", nb)

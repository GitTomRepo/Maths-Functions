# PYTHON_3
# Author : GitTomRepo
# Link : https://github.com/GitTomRepo/Maths-Functions/blob/main/newton-s_pair.py

from math import *
a = float(input("a = "))
b = float(input("b = "))
n = int(input("n = "))
nb = float(0)
for i in range (0, n+1) :
    combinaison = (factorial(n) / (factorial(i) * factorial(n - i)))
    nb = nb + (combinaison) * (a**(n-i)) * (b**i)
print("Nombre : ", nb)

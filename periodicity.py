# PYTHON_3
# Author : GitTomRepo
# Link : https://github.com/GitTomRepo/Maths-Functions/blob/main/periodicity.py

number = int(input("Number : "))
diviseur = int(input("Divider : "))
valeur_ref = number % diviseur
valeur_post = number**2 % diviseur

i = 3

while valeur_post != valeur_ref :
    valeur_post = number**i % diviseur
    i += 1
    print(valeur_post)

p = i-2
print("Periodicite : ", p)

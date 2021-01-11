# PYTHON_3
# Author : GitTomRepo
# Link : https://github.com/GitTomRepo/Maths-Functions/blob/main/reste.py

number_without_f = float(input("Number : "))
factor = float(input("Factor : "))
diviseur = int(input("Divider : "))

congru_1 = number_without_f % diviseur
print(number_without_f, "congrus", congru_1, "modulo", diviseur)

valeur_ref = congru_1 % diviseur
valeur_post = congru_1**2 % diviseur

i = 3
while valeur_post != valeur_ref :
    valeur_post = congru_1**i % diviseur
    i += 1

p = float(i-2)
print("Periodicite : ", p)

r_period_factor = factor % p
r_final = congru_1**(p+r_period_factor) % diviseur

print("Le reste de", number_without_f, "puissance", factor, "est de ", r_final)

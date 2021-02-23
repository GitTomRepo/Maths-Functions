a = int(input("a = "))
b = int(input("b = "))
r = [a%b, b%(a%b)]
while r[-1] != 0 :
    r.append(r[-2]%r[-1])
print("PGCD ({}; {}) = {}".format(a, b, r[-2]))

# PYTHON_3
# Author : GitTomRepo
# Link :

import random
caracter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "&", "~", "#", "{", "(", "[", "-", "|", "è", "_", "ç", "^", "à", "@", ")", "]", "=", "}"]
code = []
for i in range (26) :
    code.insert(-1, caracter[random.randint(0, 54)])
print("".join(code))
final_code = str("".join(code))

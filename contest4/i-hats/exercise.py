import math

def fact_n(n):
    if n == 0:
        value = 1
    elif n == 1:
        value = 0
    else:
        value = (n-1)*(fact_n(n-1)+fact_n(n-2))
    return value

t = int(input())

for i in range(t):
    n = int(input())

    nom = int(fact_n(n))
    den = int(math.factorial(n))
    print(str(nom) + '/' + str(den))
import math

n = int(input())

n_5 = int(math.factorial(n)/(math.factorial(5)*math.factorial(n-5)))
n_6 = int(math.factorial(n)/(math.factorial(6)*math.factorial(n-6)))
n_7 = int(math.factorial(n)/(math.factorial(7)*math.factorial(n-7)))

print(int(n_5+n_6+n_7))
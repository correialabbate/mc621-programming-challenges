from sys import stdin

def special_permutation(n, m):
    mul = 1
    for i in range(n-m+1, n+1):
        mul = mul * i
        while mul%10 == 0:
            mul = int(mul/10)
    return mul

for line in stdin:
    if line == '':
        break
    line = line.split()
    print(int(special_permutation(int(line[0]), int(line[1]))%10))
import math

def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n%i == 0:
                return False
        return True

n = int(input())

if n == 3 or n == 2:
    print("-1")
else:
    if not is_prime(n-2):
        print("-1")
    else:
        print(f'2 {n-2}')
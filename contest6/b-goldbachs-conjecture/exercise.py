def is_prime(list_of_primes, n):
    if n in list_of_primes:
        return True
    else:
        if n == 2:
            return True
        for i in range(3,int(n/2),2):
            if (n%i) == 0:
                return False
        return True

n = int(input())

list_of_primes = []

while (n != 0):
    if(n == 4):
        print(f'{n} = 2 + 2')
    else:
        for i in range(3, n-1, 2):
            if is_prime(list_of_primes, i):
                if i not in list_of_primes:
                    list_of_primes.append(i)
                if is_prime(list_of_primes,(n-i)):
                    if (n-i) not in list_of_primes:
                        list_of_primes.append(n-i)
                    print(f'{n} = {i} + {n-i}')
                    break

    n = int(input())
prime_alphabet = 'BCEGKMQSW'

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    s_len = len(s)
    total = 0

    for prime_letter in prime_alphabet:
        if prime_letter in s:
            total += 1

    for idx, letter in enumerate(s):
        if letter in prime_alphabet:
            total = total + (s_len - 1) + idx*(s_len - idx - 1)
    print(total)
    
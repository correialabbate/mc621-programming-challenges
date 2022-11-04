t = int(input())

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for _ in range(t):
    w = str(input())
    ans = alphabet.index(w[0])*25
    if(alphabet.index(w[1]) < alphabet.index(w[0])):
        ans += alphabet.index(w[1]) + 1
    else:
        ans += alphabet.index(w[1])
    print(ans)

def is_palindromic(s):
    return s == s[::-1]

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    found = False

    for idx, c in enumerate(s):
        if idx >= n//2:
            break
        if found:
            ans += 1
            continue
        aux = s[:idx] + s[idx+1:]
        if is_palindromic(aux):
            ans += 1
            found = True
    if n%2 == 0:
        ans = ans*2
    else:
        ans = ans*2 + 1
    print(ans)
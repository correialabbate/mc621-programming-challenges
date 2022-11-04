def is_palindrome(s):
    return s == s[::-1]

t = int(input())

for _ in range(t):
    s = str(input())

    printed = False
    for i in range(1,len(s)):
        if is_palindrome(s[:i]) and is_palindrome(s[i:]):
            print("alindrome")
            printed = True
            break

    if not printed:
        if is_palindrome(s):
            print("palindrome")
        else:
            print("simple")

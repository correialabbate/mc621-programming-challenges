alphabet_upper = 'abcdefghijklmnopqrstuvwxyz'

t = int(input())

for _ in range(t):
    len_s = int(input())
    s = input()

    reverse_s = s[::-1]
    reverse_ans = ""

    i = 0
    while i < (len_s):
        if reverse_s[i] == '0':
            pos = int(reverse_s[i+2] + reverse_s[i+1])
            reverse_ans = reverse_ans + alphabet_upper[pos-1]
            i = i + 3
        else:
            pos = int(reverse_s[i])
            reverse_ans = reverse_ans + alphabet_upper[pos-1]
            i = i + 1
        
    print(reverse_ans[::-1])

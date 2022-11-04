t = str(input())

t_without_a = t.replace('a', '')
sep = len(t)-int(len(t_without_a)/2)

s = t[:sep]
s_without_a = s.replace('a', '')

s_linha = t[sep:]

if s_without_a == s_linha:
    print(s)
else:
    print(':(')
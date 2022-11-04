t = int(input())

for _ in range(t):
    a, b = map(str, input().split())
    
    if a == b:
        print('=')
    else:
        a_len = len(a)
        b_len = len(b)
        if 'S' in a:
            if 'S' in b:
                if a_len > b_len:
                    print('<')
                else:
                    print('>')
            else:
                print('<')
        elif 'M' in a:
            if 'S' in b:
                print('>')
            else:
                print('<')
        else:
            if 'L' in b:
                if a_len > b_len:
                    print('>')
                else:
                    print('<')
            else:
                print('>')
                
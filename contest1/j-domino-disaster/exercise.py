n_tests = int(input())

for i in range(n_tests):
    n_columns = int(input())
    d_pieces = str(input())
    answer = ''
    for c in d_pieces:
        if c == 'U':
            answer += 'D'
        elif c == 'D':
            answer += 'U'
        elif c == 'L':
            answer += 'L'
        else:
            answer += 'R'
    print(answer)
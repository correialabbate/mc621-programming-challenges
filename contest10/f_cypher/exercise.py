t = int(input())

for _ in range(t):
    n = int(input())
    wheel = [int(x) for x in input().split()]
    ans = []

    for i in range(n):
        n_moves, moves = map(str, input().split())

        number_d = moves.count('D')
        number_u = moves.count('U')
        moves_revert = number_d - number_u
        val = (wheel[i] + moves_revert)%10
        ans.append(val)
    
    print(*ans)

# There is an integer n without zeros in its decimal representation. Alice and Bob are playing a game with this integer. Alice starts first. They play the game in turns.

# On her turn, Alice must swap any two digits of the integer that are on different positions. Bob on his turn always removes the last digit of the integer. The game ends when there is only one digit left.

# You have to find the smallest integer Alice can get in the end, if she plays optimally.

t = int(input())

for _ in range(t):
    n = input()
    if len(n) == 2:
        ans = n[1]
    else:
        ans = min(n)

    print(ans)
t = int(input())

for i in range(t):
    n = int(input())

    permutation = [*range(2,n+1)]
    permutation.append(1)
    
    print(*permutation)
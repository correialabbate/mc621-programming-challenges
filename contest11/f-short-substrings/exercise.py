# Alice guesses the strings that Bob made for her.
# 
# At first, Bob came up with the secret string aa consisting of lowercase English letters. The string aa has a length of 22 or more characters. Then, from string aa he builds a new string b and offers Alice the string b so that she can guess the string a.
# 
# Bob builds b from a as follows: he writes all the substrings of length 2 of the string a in the order from left to right, and then joins them in the same order into the string b.
# 
# For example, if Bob came up with the string a="abac", then all the substrings of length 22 of the string a are: "ab", "ba", "ac". Therefore, the string b="abbaac".
# 
# You are given the string b. Help Alice to guess the string a that Bob came up with. It is guaranteed that b was built according to the algorithm given above. It can be proved that the answer to the problem is unique.

t = int(input())

for _ in range(t):
    b = input()
    a = b[0]
    aux = b[1:-1]
    while len(aux) > 0:
        a += aux[0]
        aux = aux[2:]
    a += b[-1]
    print(a)
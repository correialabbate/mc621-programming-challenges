alphabet = 'abcdefghijklmnopqrstuvwxyz'

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    s = input()
    letter_count = {}

    letters_in_s = []
    for letter in s:
        if letter not in letters_in_s:
            letters_in_s.append(letter)
    letters_in_s.sort()

    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    n_discovered_letter = 0
    n_row = 1
    ans = ""

    for idx, letter in enumerate(alphabet):
        if n_discovered_letter < k:
            if letter not in letter_count:
                missing_letter_number = k - n_discovered_letter
                ans += missing_letter_number*alphabet[idx]
                n_discovered_letter += missing_letter_number
                break
            elif letter_count[letter] < (k - n_discovered_letter):
                missing_letter_number = k - n_discovered_letter - letter_count[letter]
                ans += missing_letter_number*alphabet[idx]
                n_discovered_letter += missing_letter_number
                if n_row == int(n/k):
                    ans += letter_count[letter]*alphabet[idx+1]
                    n_discovered_letter += letter_count[letter]
                n_row += 1
            elif letter_count[letter] >= (k - n_discovered_letter):
                if n_row == int(n/k):
                    ans += (k - n_discovered_letter)*alphabet[idx+1]
                    n_discovered_letter += (k - n_discovered_letter)
                    break
                else:
                    n_row += 1
        else:
            break

    print(''.join(sorted(ans, reverse = True)))
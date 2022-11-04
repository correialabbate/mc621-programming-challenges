name = input()

valid_letters = "AHIMOTUVWXY"

for i in name:
    if not i in valid_letters:
        print('NO')
        exit()

reverted_name = name[::-1]
if not reverted_name == name:
    print('NO')
    exit()

print('YES')

t = int(input())

for _ in range(t):
    s = input()
    
    same_char_strs = []
    i = 0

    while i < len(s):
        temp_str = s[i]
        while i < (len(s)-1) and s[i] == s[i+1]:
            temp_str += s[i+1]
            i += 1
        same_char_strs.append(temp_str)

        i += 1
    
    strings_even_size = []
    for string in same_char_strs:
        if len(string) % 2 == 0:
            strings_even_size.append(string)
    
    for string in strings_even_size:
        same_char_strs.remove(string)
    
    # total = len(same_char_strs)
    # for i in range(len(same_char_strs)-1):
    #     for j in range(i+1,same_char_strs):
    #         if same_char_strs[i][0] == same_char_strs[j][0]:
    #             total = total - len(same_char_strs)

        



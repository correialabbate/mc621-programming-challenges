# You may have already known that a standard ICPC team consists of exactly three members. The perfect team however has more restrictions. A student can have some specialization: coder or mathematician. She/he can have no specialization, but can't have both at the same time.

# So the team is considered perfect if it includes at least one coder, at least one mathematician and it consists of exactly three members.

# You are a coach at a very large university and you know that cc of your students are coders, mm are mathematicians and xx have no specialization.

# What is the maximum number of full perfect teams you can distribute them into?

# Note that some students can be left without a team and each student can be a part of no more than one team.

# You are also asked to answer qq independent queries.

q = int(input())
i = 2
for _ in range(q):
    c, m, x = map(int, input().split())
    
    max_num_teams = min(c, m)
    if c+m+x >= (max_num_teams*3):
        ans = max_num_teams
    else:
        if min == 1 and (c > 1 or m > 1):
            ans = 1
        else:
            ans = int((c+m+x)/3)
    print(ans)
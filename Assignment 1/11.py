s = input("Enter :").split(" ")
k = dict()
for i in range(0,len(s)):
    c = 0
    for j in range(i, len(s)):
        if s[i] == s[j]:
            c +=1

    if s[i] not in k:
        k[s[i]] = c

[print(i,": ",k[i]) for i in k]
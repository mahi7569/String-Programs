s=input()
res=''
for i in range(len(s)):
    if i%2==0:
        if s[i].islower():
            res+=chr(ord(s[i])-32)
        else:
            res+=s[i]
    else:
        res+=s[i]
print(res)
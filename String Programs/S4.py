s=input()
res=s[0]
max=s.count(s[0])
for i in s:
    if s.count(i)>max:
        max=s.count(i)
        res=i 
print(res)
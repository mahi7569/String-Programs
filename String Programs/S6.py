s=input()
res=''
for i in s:
    if s.count(i)==1:
        res+=i 
print(res[0])
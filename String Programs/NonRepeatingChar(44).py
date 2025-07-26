s=input()
c=0
res=''
for i in s:
    if s.count(i)==1:
        res+=i 
        c+=1
print(res,c)
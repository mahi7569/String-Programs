s=input()
res=''
l=[]
for i in s:
    l.append(s.count(i))
for i in s:
    if max(l)==s.count(i):
        if i not in res:
            res+=i 
print(res) 

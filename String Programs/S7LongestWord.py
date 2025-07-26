s=input()  
r=s.split()
max=str(len(r[0]))
res=r[0]
for i in r:
    if str(len(i))>max:
        max=i 
        res=i 
print(res)  

#Method-2:
'''s=input().split()
res=[]
for i in s:
    res.append((len(i),i)) 
print(sorted(res)[-1][1])'''






s=input()   #1210
d=0
l=0
for i in s:
    if str(s.count(str(d)))==i:
        l+=1
    d+=1
if l==len(s):
    print(s,"is a Auto Biographic Number")
else:
    print(s,"is Not a Auto Biographic Number")  

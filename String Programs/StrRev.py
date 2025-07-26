'''s=input()
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')'''

s=input()
l=list(s)
i,j=0,len(s)-1
while(i<j):
    t=l[i]
    l[i]=l[j]
    l[j]=t 
    i+=1
    j-=1
print(''.join(l)) 
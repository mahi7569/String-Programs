s=input()
l=list(s)
i=0
j=len(l)-1
while i<j:
    if s[i].isdigit() and s[j].isdigit():
        t=l[i]
        l[i]=l[j]
        l[j]=t
        i+=1 
        j-=1 
    else:
        if not s[i].isdigit():
            i+=1 
        if not s[j].isdigit():
            j-=1 
print(''.join(l))

s=input()
l=list(s)
i=0
j=len(l)-1
while i<j:
    if s[i].isalnum() and s[j].isalnum():
        t=l[i]
        l[i]=l[j]
        l[j]=t
        i+=1 
        j-=1 
    else:
        if not s[i].isalnum():
            i+=1 
        if not s[j].isalnum():
            j-=1 
print(''.join(l))

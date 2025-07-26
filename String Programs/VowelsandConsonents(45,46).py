s=input()
co,c=0,0
res=''
r=''
re='aeiouAEIOU'
for i in s:
    if i.isalpha() and not i.isdigit():
        if i in re:
            res+=i 
            co+=1
        else:
            r+=i 
            c+=1
print(res,co)
print(r,c)

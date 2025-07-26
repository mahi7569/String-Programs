s=input()
al,d,sp=0,0,0
for i in s:
    if i.isalpha():
        al+=1
    elif i.isdigit():
        d+=1 
    else:
        sp+=1
print(al,d,sp)
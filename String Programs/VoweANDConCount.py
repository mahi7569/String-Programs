s=input()
al="aeiouAEIOU"
c=0
cu=0
for i in s:
    if i.isalpha():
        if i in al: 
            c+=1
        else:
            cu+=1
print(c,cu) 
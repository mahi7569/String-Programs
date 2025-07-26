s=input()
res=''
for i in s:
    if i.islower():
        res+=i.upper()
    else:
        res+=i.lower()
print(res) 
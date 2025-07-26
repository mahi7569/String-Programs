s=input()
res=''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        res+=chr(ord(i)-32)
print(res)    
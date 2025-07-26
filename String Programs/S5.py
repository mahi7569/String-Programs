'''s=input()   # Reverse each word in a string
res=''
for i in s.split():
    res+=i[::-1]+' '
print(res)'''

s=input().split()
l=len(s[0])
res=s[0]
for i in s:
    if len(i)>l:
        l=len(i)
        res=i 
print(res)

s=input()
t=s[0]
res=''
for i in s[1:]:
    if i==t:
        res+='#'
    else:
        res+=i 
print(t+res)

s=input()
'''l=s[0]
s1=s.replace(l,'#')
print(l+s1[1:])'''

#without repalce
t=s[0]
res=''
for i in s[1:]:
    if i==t:
        res+='#'
    else:
        res+=i 
print(t+res) 
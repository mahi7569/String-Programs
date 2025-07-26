'''s=input()
ss=input()
l=[]
m,n=len(s),len(ss)
for i in range(0,(m-n)+1):
    if s[i:i+n]==ss:
        l.append(i)
print(l) '''

'''s=input().split()
l=[]
c=0
al='aeiouAEIOU'
for i in s:
    if i[0] in al:
        l.append(i)
        c+=1
print(l)
print(c)'''

'''s=input()
res=''
for i in s.split():
    res+=i[0].upper()+i[1:]+' '
print(res)'''

'''s=input()
res=''
for i in s:
    if i not in res:
        res+=i 
print(res)'''

s=input().split('.')
if len(s)==4:
    for i in s:
        if (i).isdigit() and (int(i)>=0 and int(i)<=255) and (i=='0' or not i.startswith("0")):
            print("True")
            break
        else:
            print("False")
else:
    print("No")




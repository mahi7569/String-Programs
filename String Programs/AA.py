'''a=int(input())
b=int(input())
c=int(input())
d=int(input())
l=[]
s=str(a)+str(b)+str(c)+str(d)
for i in s:
    l.append(s.count(i))
for i in s:
    if max(l)==s.count(i):
        print(i)
        break'''

'''s=input()
res=''
for i in s:
    if i=='.':
        continue
    else:
        res+=i 
if res==res[::-1]:
    print(res)
else:
    print("-1")  '''

'''def sr(n):
    div=1
    sum=0 
    for i in n:
        if i=='1':
            sum+=div 
        div=div*2
    return sum 
s=input()
s1=input()
r=sr(s)
t=sr(s1)
res=r+t 
re=''
while res!=0:
    re+=str(res%2)
    res//=2
print(re[::-1])'''


'''s=input()
res=''
for i in s:
    if i.isalnum():
        res+=i 
if res==res[::-1]:
    print("True")
else:
    print("False") '''

'''s=input()
s1=input()
res=''
for i in s.split():
    if i==s1:
        res+=i
        break
    else:
        res+=i+" "
print(res)'''

'''s=input()
l1=s.split()
ss=input()
l=[]
for i in range(len(l1)):
    if l1[i]==ss:
        l.append(i)
print(l)'''

'''s=input()
print(s.strip())
#print(s.lstrip('-'))
#print(s.rstrip('-'))'''


#Instance methods
'''class A:
    def __init__(self,a1,b): 
        self.a1=a1
        self.b=b
    def show(self):
        print(self.a1,self.b)
    def update(self,new):
        self.a1=new 
        print(self.a1,self.b)
    def delete(self):
        del self.a1
        #print(self.b)
        print(self.a1)
a=A(12,34)
a.show() # internally -->  A.show(a,12,34)
a.update(1) 
a.delete()   '''

'''n=int(input())
while(True):
    s=0
    l=[]
    for i in str(n):
        s+=int(i)*int(i)
    if s==1:
        print("Yes")
        break 
    else:
        if s not in l:
            l.append(s)
        else:
            print("No")
            break 
    n=s '''




l=input().split()
el=[i for i in l if i[0].isupper()]
print(el)

'''s=input()    #print string in reverse order without changing special character position
l=list(s)
i=0
j=len(l)-1
while i<j:
    if l[i].isalnum() and l[j].isalnum():
        t=l[i]
        l[i]=l[j]
        l[j]=t 
        i+=1
        j-=1
    else:
        if not l[i].isalnum():
            i+=1
        if not l[j].isalnum():
            j-=1
print(''.join(l))'''

'''s=input()  # print vowels and consonenets in a string in acending order along with there counts
al="aeiouAEIOU"
res,re='',''
co,c=0,0
for i in s:
    if i.isalpha() and not i.isdigit():
        if i in al:
            res+=i 
            co+=1
        else:
            re+=i 
            c+=1
print(''.join(sorted(res)),co)
print(''.join(sorted(re)),c)'''


'''def prime(n):  # circular prime
    if n<=1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
def is_prime(n):
    s=str(n)
    for i in range(len(s)):
        r=int(s[i:]+s[:i])
        if prime(r):
            return 1
        else:
            return 0
n=int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")'''


'''def square(n):
    s=0
    for i in str(n):
        s+=int(i)*int(i)
    return s 
s=input()
l=s.split(',')
for i in l:
    r=i.split(":")
    m=r[0]
    n=r[1]
    #k=square(n)
    if square(n)%2==0:
        res=m[-1]+m[0:-1]
    else:
        res=m[2:]+m[0:2]
    print(res) '''


'''s=input()
l=list(s)
i=0
j=len(s)-1
while i<j:
    if l[i].isalnum() and l[j].isalnum():
        t=l[i]
        l[i]=l[j]
        l[j]=t 
        i+=1
        j-=1
    else:
        if not l[i].isalnum():
            i+=1
        if not l[j].isalnum():
            j-=1
print(''.join(l))'''


'''s=input()
n=int(input())
print(s[n:])'''


'''Problem Statement:
Write a program to replace all instances of multiple consecutive spaces in a string with a single space.

Test Cases:

Input: "hello world" → Output: "hello world"

Input: "Python is fun" → Output: "Python is fun" '''


'''s=input().split()
l1=[]
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = range(1, 27)
for i in range(len(str(s))-1):
    for j in range(len(str(s))-1,-1,-1):
        sum=(int(str(s)[0])-int(str(s)[-1])) 
        l1.append(str(sum))
        i+=1
        j-=1 
print(l1)'''



'''s=input() 
res=''    
for i in s:
    if i not in res:
        d=s.count(i)
        res+=i 
        print(f"{i} - {d}")  '''

s1=input()  #CTS
s2=input()
res=''
for i in set(s1):
    if i in s2:
        res+=int(i)
print(res) 







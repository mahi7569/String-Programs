
'''l=list(map(int,input().split()))
for i in range(0,len(l)):
    s1=0
    s2=0
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            s1+=l[j]
        else:
            s2+=l[j]
    print(s1*s2,end=' ') '''

#program-2
'''l=list(map(int,input().split()))   (program-2)
r=sorted(l) 
s=0
for i in r:
    s+=abs(r.index(i)-l.index(i))*i
print(s)    '''


#Problem-3
'''def square(n):   #rotate the word based on the sum of squares of a number
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

#pro-4
'''l=list(map(int,input().split()))  #program to print all the data items of a list whose index is divisible by 3 exactly 
for i in range(len(l)):
    if i%3==0:
        print(l[i],end=' ')'''

#pro-5
l=list(map(int,input().split()))
for i in range(len(l)):
    print((i,l[i]),end=' ')





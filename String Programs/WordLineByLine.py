'''s=input().split()
for i in s:
    print(i)'''
s=input()
for i in s:
    if i.isspace():
        print('')
    else:
        print(i,end='')


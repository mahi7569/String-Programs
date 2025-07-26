'''s=input()   # Remove the duplicates in a string  or Print non repeating characters  ((1))
res=''
for i in s:
    if s.count(i)==1:  
        res+=i          
print(res)'''

''''s=input()  # print unique eleemnts in a string  ((2))
res=''
for i in s:
    if i not in res:
        res+=i 
print(res)'''

'''s=input() Print First character in each word upper in a string  ((3))
res=''
for i in s.split():
    res+=i[0].upper()+i[1:]+' '
print(res)'''

'''s=input()        # Print First character in each word upper in a string --> Method-2     ((4))
print(s.title())'''

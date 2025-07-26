s=input()
al="aeiouAEIOU"
for i in s:
    if i in al:  # use 'not in' for consonents
        print(i,end=' ')

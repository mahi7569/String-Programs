s1=input()
s2=input()
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("NO")
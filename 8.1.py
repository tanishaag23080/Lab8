a=input("Enter a string ")
vowel=0
consonent=0
number=0
space=0
other=0
a.lower()
for i in a:
    if i in"aeiou":
        vowel+=1
    elif i in"bcdfghjklmnpqrstvwxyz":
        consonent+=1
    elif i in "0123456789":
        number+=1
    elif i in " ":
        space+=1
    else:
        other+=1
print("Vowels",vowel)
print("Consonents",consonent)
print("Numbers",number)
print("Spaces",space)
print("Others",other)
        
sen=input("Enter sentence")
word=""
p=[]
for i in sen:
    if i.isalpha():
        word+=i
    else:
        p.append(len(word))
        word=''
p.append(len(word))
print(" ".join(map(str,p)))
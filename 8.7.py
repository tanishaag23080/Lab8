sen=input("Enter a sentence").strip()
change=0
for i in range(len(sen)//2):
    if sen[i]!=sen[len(sen)-i-1]:
        change+=1
    else:
        continue
print("Changes needed:",change)
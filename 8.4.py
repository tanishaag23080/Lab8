string=input("Enter a string")
chrt=input("Enter character")
count=0
p=[]
for i in range(len(string)):
    if chrt==string[i]:
        count+=1
        p.append(i)
if count==0:
    print("count:",count)
    print("position:",-1)
else:
    print("count:",count)
    print("position:"," ".join(map(str,p)))
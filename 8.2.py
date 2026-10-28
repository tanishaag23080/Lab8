a=input("Enter a string")
a.lower()
c=""
for i in range(len(a)):
    if i%2==0:
        c+=a[i].upper()
    else:
        c+=a[i].lower()
print(c)
    

mess=input("Enter string")
shift=int(input("Enter "))
encoded=''
for i in mess:
    if i==" ":
        encoded+=" "
    else:
        if ord(i)+shift>=123:
            encoded+=chr(ord(i)+shift-26)
        else:
            encoded+=chr(ord(i)+shift)
        
print(encoded)
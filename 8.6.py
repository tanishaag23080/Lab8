plate=input("Enter number plate").strip()
if len(plate)==10 and plate[0:2]=="RJ":
    if (plate[0].isupper() and plate[1].isupper() and
        plate[2].isdigit() and plate[3].isdigit() and
        plate[4].isupper() and plate[5].isupper() and
        plate[6].isdigit() and plate[7].isdigit() and
        plate[8].isdigit() and plate[9].isdigit()):
        print("True")
    else:
        print("False")
else:
    print("False")
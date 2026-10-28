s = input("Enter string").strip()

best=''
best_len=0

current=''
current_len=0

for ch in s:
    if ch == current:
        current_len+=1
    else:
        current=ch
        current_len=1
    if current_len>best_len:
        best_len=current_len
        best=current

print(best,best_len)
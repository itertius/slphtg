num = input()

check = [0 for i in range(10)]

for i in range(len(num)) :
    if 0 <= int(num[i]) <= 9 :
        check[int(num[i])-int('0')] = 1

valid = True
for i in range(10) :
    if check[i]==0 : 
        valid=False

if valid :
    print("None")
else :
    missing = [str(i) for i in range(10) if check[i]==0]
    print(",".join(missing))
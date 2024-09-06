arr = []
while 1 :
    temp = input()
    if temp=="q" and len(arr)==0 :
        print("No Data")
        exit(0)
    elif temp=="q" :
        break
    arr.append(float(temp))

sum = 0
for i in range(len(arr)) :
    sum+=arr[i]

print("{:.2f}".format(sum/len(arr)))
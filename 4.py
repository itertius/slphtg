arr = []
for i in range(0, 5) :
    arr.append(int(input()))

for i in range(len(arr)) :
    for j in range(0, len(arr)-i-1) :
        if arr[i]>arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr[2])
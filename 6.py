arr = input().split()
for i in range(0, 4) : arr[i]=float(arr[i])

arr.sort()

print((arr[1]+arr[2])/2)
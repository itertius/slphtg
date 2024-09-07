lst = []
up = []
while 1 :
    temp=input()
    if temp=="q" :
        up = input().split(" ")
        break
    lst.append(temp.split(" "))

print(lst)

for i in range(len(lst)) :
    for j in range(0, len(lst)-i-1) :
        if int(lst[i][0])>int(lst[j+1][0]) :
            temp = int(lst[i][0])
            lst[i][0] = int(lst[j+1][0])
            lst[j+1][0] = temp

print(lst)

print(up)

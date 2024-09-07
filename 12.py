# not finished

lst = []
up = []
while 1 :
    temp=input()
    if temp=="q" :
        up = input().split(" ")
        break
    lst.append(temp.split(" "))

# print(lst)

for i in range(len(lst)) :
    if i<=len(up)-1 :
        up[i] = int(up[i])
    for j in range(0, len(lst)-i-1) :
        lst[i][0] = int(lst[i][0])
        lst[j+1][0] = int(lst[j+1][0])
        # print(i, j)
        if lst[i][0]>lst[j+1][0] :
            lst[j], lst[j+1] = lst[j+1], lst[j]

# print(lst)
# print(up)

check = []
for ilst in range(len(lst)) :
    # print(ilst[0])
    for jup in up :
        # print("log")
        print(jup)
        if lst[ilst][0]==jup :
            print(lst[ilst][0] , "#1")
            print(jup , "#2")
            # print(lst[i][1] , "#3")
            match lst[i][1] :
                case "B+" :
                    lst[i][1]="A"
                    check.append(lst[i][1])
                    # print(lst[i][1])
                case "B" :
                    lst[i][1]="B+"
                    check.append(lst[i][1])
                    # print(lst[i][1])
                case "C+" :
                    lst[i][1]="B"
                    check.append(lst[i][1])
                    # print(lst[i][1])
                case "C" :
                    lst[i][1]="C+"
                    check.append(lst[i][1])
                    # print(lst[i][1])
                case "D+" :
                    lst[i][1]="C"
                    check.append(lst[i][1])
                    # print(lst[i][1])
                case "D" :
                    lst[i][1]="D+"
                    check.append(lst[i][1])
                    # print(lst[i][1])
                case "F" :
                    lst[i][1]="D"
                    check.append(lst[i][1])
                    # print(lst[i][1])

print(lst)

print(check)

# if lst[0][1]=="A" :
#     print("True")

# B+ -> A | B -> B+ | C+ -> B | C -> C+ | D+ -> C | D -> D+ | F -> D
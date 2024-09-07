# nearly finished

lst = []
up = []

while True :
    temp=input()
    if temp=="q" :
        up = input().split(" ")
        break
    lst.append(temp.split(" "))

grade_dict = {
    "B+" : "A",
    "B" : "B+",
    "C+" : "C",
    "D+" : "C",
    "D" : "D+",
    "F" : "D"
}

for i in range(len(lst)) :
    if i<=len(up)-1 :
        up[i] = int(up[i])
    for j in range(len(lst)-i-1) :
        lst[i][0] = int(lst[i][0])
        lst[j+1][0] = int(lst[j+1][0])
        if lst[i][0]>lst[j+1][0] :
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(len(lst)) :
    for iup in up :
        if iup==lst[i][0] :
            origin = lst[i][1]
            if origin in grade_dict :
                lst[i][1] = grade_dict[origin]

print(lst)
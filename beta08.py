num = list(map(int, input().split()))
num.sort()

string = input()

check = []
for i in range(3) :
    match string[i] :
        case "A" :
            check.append(str(num[0]))
        case "B" :
            check.append(str(num[1]))
        case "C" :
            check.append(str(num[2]))

print(" ".join(check))
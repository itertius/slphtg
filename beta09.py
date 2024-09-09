string = input()

check = [1, 0, 0]
for i in range(len(string)) :
    match string[i] :
        case "A" :
            check[0], check[1] = check[1], check[0]
        case "B" :
            check[1], check[2] = check[2], check[1]
        case "C" :
            check[0], check[2] = check[2], check[0]

for i in range(3) :
    if check[i]==1 :
        print(i+1)
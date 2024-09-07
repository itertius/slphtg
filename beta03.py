m, n = map(int, input().split())

arri = []
for _ in range(m) :
    arri.append(list(map(int, input().split())))

arrj = []
for _ in range(m) :
    arrj.append(list(map(int, input().split())))

for i in range(m) :
    for j in range(n) :
        print(arri[i][j] + arrj[i][j], end=' ')
    print()

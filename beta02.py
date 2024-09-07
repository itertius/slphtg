n = int(input())

lst = []
for i in range(n) :
    lst.append(int(input()))

lst.sort()

print(lst[0], lst[n-1], sep="\n")
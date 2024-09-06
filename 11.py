lst = list(map(int, input().split(" ")))

unq = sorted(set(lst))

count = len(unq)

ind = []
for val in unq :
    ind_lst = [i for i, x in enumerate(lst) if x==val]
    ind.append(ind_lst[:10])

print(count)

# not finished
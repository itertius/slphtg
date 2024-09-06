# not finished

lst = []
up = []
while 1 :
    temp=input()
    if temp=="q" :
        up = input().split(" ")
        break
    lst.append(temp.split(" "))

print(lst)
print(up)

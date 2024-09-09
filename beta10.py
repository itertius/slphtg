ans = set()
for i in range(10) :
    num = int(input())
    ans.add(num%42)

print(len(ans))
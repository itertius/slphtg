x = input()
n = int(input())

if n>=len(x) :
   print("0"*(n-len(x)) + x)
else :
   print(x)
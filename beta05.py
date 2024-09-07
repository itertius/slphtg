import math

a, b = map(float, input().split())

c = math.sqrt(a**2 + b**2)

print("{:.6f}".format(c))
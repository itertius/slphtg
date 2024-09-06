d,m,y = [int(e) for e in input().split()]

d+=15
match m :
    case 4 | 6 | 9 | 11 :
        n=30
    case 2 :
        if y%400==0 | y%4==0 & y%100!=0 :
            n=29
        else :
            n=28
    case _ :
        n=31

if d>n :
    d-=n
    m+=1
if m>12 :
    m-=12
    y+=1

print(f"{d}/{m}/{y}")
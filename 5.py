x = float(input())

match x :
    case x if x>=80 :
        print("A")
    case x if x>=70 :
        print("B")
    case x if x>= 60 :
        print("C")
    case x if x>=50 :
        print("D")
    case _ :
        print("F")
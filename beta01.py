sum = int(input()) + int(input()) + int(input())

match sum :
    case sum if sum>=80 :
        print("A")
    case sum if sum>=75 :
        print("B+")
    case sum if sum>=70 :
        print("B")
    case sum if sum>=65 :
        print("C+")
    case sum if sum>=60 :
        print("C")
    case sum if sum>=55 :
        print("D+")
    case sum if sum>=50 :
        print("D")
    case _ :
        print("F")
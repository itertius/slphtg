x = int(input())

check = ["", ""]
match x :
    case x if x>0 :
        if x%2==0 :
            check = ["positive", "even"]
        else :
            check = ["positive", "odd"]
    case x if x==0 :
        if x%2==0 :
            check = ["zero", "even"]
    case x if x<0 :
        if x%2==0 :
            check = ["negative", "even"]
        else :
            check = ["negative", "odd"]

print(check[0] + "\n" + check[1])
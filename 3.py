text = input().split("/")
text[1] = int(text[1])

# print(text)

month = ""
match text[1] :
    case 1 :
        month = "Jan"
    case 2 :
        month = "Feb"
    case 3 :
        month = "Mar"
    case 4 :
        month = "Api"
    case 5 :
        month = "May"
    case 6 :
        month = "Jun"
    case 7 :
        month = "Jul"
    case 8 :
        month = "Aug"
    case 9 :
        month = "Sep"
    case 10 :
        month = "Oct"
    case 11 :
        month = "Nov"
    case 12 :
        month = "Dec"
print(month , text[0] + "," + text[2])
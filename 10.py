text = input()

encode = []
current_char = text[0]
count = 0

for char in text[1:] :
    if char==current_char :
        count+=1
    else :
        encode.append(f"{current_char} {count}")
        current_char=char
        count=1

encode.append(f"{current_char} {count}")

print(" ".join(encode))
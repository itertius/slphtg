# Initialize lists
lst = []
up = []

# Input data
while True:
    temp = input()
    if temp == "q":
        up = input().split()
        break
    lst.append(temp.split())

# Sort lst based on the first element (which is assumed to be an integer)
lst.sort(key=lambda x: int(x[0]))

# Print sorted lst (for debugging)
# print(lst)
# print(up)

# Dictionary for grade mapping
grade_map = {
    "B+": "A",
    "B": "B+",
    "C+": "B",
    "C": "C+",
    "D+": "C",
    "D": "D+",
    "F": "D"
}

# Update grades based on `up`
check = []
for ilst in range(len(lst)):
    # Check if the grade is in `up`
    if int(lst[ilst][0]) in map(int, up):
        # Update the grade
        original_grade = lst[ilst][1]
        if original_grade in grade_map:
            lst[ilst][1] = grade_map[original_grade]
            check.append(lst[ilst][1])

# Print updated lst and check lists
print(lst)
print(check)

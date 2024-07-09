# Part c

marks = []

# Use a while loop to get 5 marks from the user
count = 0
while count < 5:
    try:
        mark = float(input(f"Enter mark {count + 1}: "))
        marks.append(mark)
        count += 1
    except ValueError:
        print("Please enter a valid mark.")

# Display the grades
for mark in marks:
    if mark > 75:
        grade = 'A'
    elif 65 <= mark <= 75:
        grade = 'B'
    elif 55 <= mark <= 64:
        grade = 'C'
    elif 45 <= mark <= 54:
        grade = 'S'
    else:
        grade = 'F'
    print(f"Mark: {mark}, Grade: {grade}")

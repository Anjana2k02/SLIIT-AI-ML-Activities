marks = []
count = 0

# input marks
while count < 10:
    m = float(input("Enter marks : "))
    if m<0:
        print("Invalid. try again")
        continue
    else:
        marks.append(m)
        count+=1



print("Maximum mark is" , max(marks)) #maximum
print("Minimum mark is ", min(marks)) #minimum

avg = sum(marks) / count
print("Average mark is ",avg) #average
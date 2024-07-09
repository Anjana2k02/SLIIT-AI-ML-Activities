#  Part d


total_sum = 0

# Input numbers until -999
while True:
    try:
        num = float(input("Enter a number (-999 to stop): "))
        if num == -999:
            break
        total_sum += num
    except ValueError:
        print("Please enter a valid number.")

# Print the sum of the numbers
print("The sum of the numbers entered is:", total_sum)

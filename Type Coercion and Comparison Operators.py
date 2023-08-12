# Get user input
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))

# Compare and provide messages
if value1 < value2:
    print("The first value is less than the second value.")
elif value1 > value2:
    print("The first value is greater than the second value.")
else:
    print("The two values are equal.")

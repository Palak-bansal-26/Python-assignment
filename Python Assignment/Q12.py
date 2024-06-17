num = input("Enter a number: ")

# Initialize sum
sum_digits = 0

for digit in num:
    sum_digits += int(digit)

# Print the result
print("The sum of digits is: ",sum_digits)

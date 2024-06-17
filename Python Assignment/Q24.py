num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Check if dividing by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Error: Invalid operator entered.")
    result = None

# Print the result if calculation was successful
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")

nums = input("Enter a list of numbers separated by spaces: ").split()

# Convert input strings to integers
nums = [float(num) for num in nums]  # Convert to float to handle decimal numbers as well

# Calculate minimum and maximum using built-in functions
min_value = min(nums)
max_value = max(nums)

# Print the results
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")

# Initialize an empty list to store lines
lines = []

# Read input lines from user until an empty line is entered
print("Enter multiple lines (press Enter twice to finish):")
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

# Print all the entered lines
print("\nThe entered lines are:")
for line in lines:
    print(line)

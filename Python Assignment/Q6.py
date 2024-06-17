# Specify the filename
filename = "output.txt"

# Open the file in read mode and read its content
with open(filename, "r") as file:
    content = file.read()

# Print the content to the console
print("The content of the file is:")
print(content)

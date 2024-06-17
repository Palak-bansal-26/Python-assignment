source_file = 'source.txt'
destination_file = 'destination.txt'

# Open the source file for reading
with open(source_file, 'r') as src:
    # Read the contents of the source file
    contents = src.read()

# Open the destination file for writing
with open(destination_file, 'w') as dst:
    # Write the contents to the destination file
    dst.write(contents)

# Print confirmation message
print(f'Contents of {source_file} have been copied to {destination_file}')

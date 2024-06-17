from collections import Counter

# Input string
input_string = "hello world"

# Use Counter from collections to count the frequency of characters
frequency = Counter(input_string)

# Print the frequency of each character
for char, count in frequency.items():
    print(f"Character: {char} - Frequency: {count}")

string1 = "listen"
string2 = "silent"

# Remove any spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if the sorted characters of both strings are equal
if sorted(string1) == sorted(string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
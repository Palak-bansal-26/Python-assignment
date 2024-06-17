string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

# Remove spaces from both strings
string1 = string1.replace(" ", "")
string2 = string2.replace(" ", "")

# Check if lengths are different
if len(string1) != len(string2):
    are_anagrams = False
else:
    # Sort characters in both strings and compare
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        are_anagrams = True
    else:
        are_anagrams = False

# Output the result
if are_anagrams:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

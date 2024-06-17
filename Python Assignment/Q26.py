input_string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

# Check if the string starts with the prefix
if input_string.startswith(prefix):
    print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
else:
    print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")

# Check if the string ends with the suffix
if input_string.endswith(suffix):
    print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
else:
    print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")

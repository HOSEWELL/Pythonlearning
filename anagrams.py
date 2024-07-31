def are_anagrams(str1, str2):

    # Check if the lengths of both strings are the same
    if len(str1) != len(str2):
        return False

    # Sort both strings and compare them
    return sorted(str1) == sorted(str2)

# Test cases
string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')


# Fix the indentation of the is_palindrome function
def is_palindrome(s):
    """Checks if a string is a palindrome, ignoring case and punctuation."""
    # Convert the string to lowercase and remove punctuation
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Read the user input and check if it is a palindrome
user_input = input("Enter a string:"" ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')


import string

def is_palindrome(s):
    # Remove punctuation, spaces, and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator).replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]

# Get input from the user
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')


# palindrome_recursive.py asks the user for a string and determines if it is palindromic using a recursive function

# import function for cleaning strings
from string_cleaner import strip_whitespace_and_punctuation_and_make_lowercase

def check_if_palindrome_recursively(phrase):
    """return True if the string is a palindrome by checking recursively"""
    # make lowercase
    phrase = phrase.lower()
    # strip whitespace and punctuation
    phrase = strip_whitespace_and_punctuation_and_make_lowercase(phrase)

    if len(phrase) == 0 or len(phrase) == 1:
        return True
    elif phrase[0] == phrase[-1]:
        return check_if_palindrome_recursively(phrase[1:-1])
    else:
        return False

# ask user for a string
user_input = input("Enter a phrase, a sentence, or multiple sentences to see if it is a palindrome! ")

# check if user_input is a palindrome recursively and return
if check_if_palindrome_recursively(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
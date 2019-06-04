# palindrome.py asks the user for a string and determines if it is palindromic

# import re library for using regular expressions
import re

def strip_whitespace_and_punctuation_and_make_lowercase(phrase):
    """remove all characters except for alphabetical letters from a string and make lowercase"""
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    return phrase.lower()

def check_if_palindrome(phrase):
    """return True if the string is a palindrome"""
    # strip whitespace and punctuation and make lowercase
    phrase = strip_whitespace_and_punctuation_and_make_lowercase(phrase)
    #check if reverse is same as normal and return
    return phrase == phrase[::-1]

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

# check if user_input is a palindrome and return
if check_if_palindrome(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")

# check if user_input is a palindrome recursively and return
if check_if_palindrome_recursively(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
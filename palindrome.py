# palindrome.py asks the user for a string and determines if it is palindromic

# import function for cleaning strings
from string_cleaner import strip_whitespace_and_punctuation_and_make_lowercase

def check_if_palindrome(phrase):
    """return True if the string is a palindrome"""
    # strip whitespace and punctuation and make lowercase
    phrase = strip_whitespace_and_punctuation_and_make_lowercase(phrase)
    #check if reverse is same as normal and return
    return phrase == phrase[::-1]

# ask user for a string
user_input = input("Enter a phrase, a sentence, or multiple sentences to see if it is a palindrome! ")

# check if user_input is a palindrome and return
if check_if_palindrome(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
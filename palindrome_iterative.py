# palindrome_iterative.py asks the user for a string and determines if it is palindromic using an iterative function

# import re library for using regular expressions
import re

def strip_whitespace_and_punctuation_and_make_lowercase(phrase):
    """remove all characters except for alphabetical letters from a string and make lowercase"""
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    return phrase.lower()

def check_if_palindrome_iteratively(phrase):
    """return True if the string is a palindrome by checking iteratively"""
    # make lowercase
    phrase = phrase.lower()
    # strip whitespace and punctuation
    phrase = strip_whitespace_and_punctuation_and_make_lowercase(phrase)

    i = 0
    is_palindrome = False
    while i < len(phrase):
        if phrase[0 + i] != phrase[-1 - i]:
            is_palindrome = False
        elif len(phrase) == 0 or len(phrase) == 1:
            is_palindrome = True
        elif phrase[0 + i] == phrase[-1 + i]:
            is_palindrome = True 
        i += 1
    return is_palindrome

# ask user for a string
user_input = input("Enter a phrase, a sentence, or multiple sentences to see if it is a palindrome! ")

# check if user_input is a palindrome iteratively and return
if check_if_palindrome_iteratively(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
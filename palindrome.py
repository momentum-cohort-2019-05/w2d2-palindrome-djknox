# palindrome.py asks the user for a string and determines if it is palindromic

# import re library for using regular expressions
import re

def strip_whitespace_and_punctuation(phrase):
    """remove all characters except for alphabetical letters from a string"""
    return re.sub(r'[^A-Za-z]', '', phrase)

def check_if_palindrome(phrase):
    """return True if the string is a palindrome"""
    # make lowercase
    phrase = phrase.lower()
    # strip whitespace and punctuation
    stripped_phrase = strip_whitespace_and_punctuation(phrase)
    #check if reverse is same as normal and return
    return stripped_phrase == stripped_phrase[::-1]

# ask user for a string
user_input = input("Enter a phrase, a sentence, or multiple sentences to see if it is a palindrome! ")

# check if palindrome and return
if check_if_palindrome(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
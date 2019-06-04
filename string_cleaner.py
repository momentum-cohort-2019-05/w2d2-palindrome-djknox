# string_cleaner.py contains a function for making a string lowercase and stripping the whitespace and punctuation

# import re library for using regular expressions
import re

def strip_whitespace_and_punctuation_and_make_lowercase(phrase):
    """remove all characters except for alphabetical letters from a string and make lowercase"""
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    return phrase.lower()
import re

# ask user for one or more sentences
user_input = input("Enter a phrase, a sentence, or multiple sentences to see if it is a palindrome! ")

# Use "is a palindrome" and "is not a palindrome" in your output in order for the tests to pass.
def check_if_palindrome(phrase):
    # strip of whitespace and punctuation
    phrase = re.sub(r'[^A-Za-z]', '', phrase)
    #check if reverse is same as normal
    phrase_reversed = phrase[::-1]
    if phrase == phrase_reversed:
        return True
    else:
        return False

if check_if_palindrome(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")

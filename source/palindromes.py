#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    print(is_palindrome_recursive(text))
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    index = 0

    #Remove White space for multiline palindromes
    text = text.strip(" ")
    print(text)
    while index < len(text):
        if text[index] == text[-index-1]:
            if index > round(len(text)/2):
                return True
            index += 1
        else:
            return False

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

    #Checking base case!!!!
    if len(text) == 0:
        return True

    #Formatting string for recursion(mixed case and punctuation)
    # Setting Initial State
    if left == None or right == None:
        cleaned_text = ""

        text = text.lower()
        for char in text:
            if char.isalpha():
                cleaned_text += char
        text = cleaned_text

        left = 0
        right = len(text)-1


    # Checking both opposite sides
    print("right {} left {}".format(text[right], text[left]))
    if text[right] == text[left]:
        if(left == round(len(text)/2)):
            print("total len {}left {} middle-ish {}".format(len(text),left, len(text)/2))
            return True
        left +=1
        right -=1
        return is_palindrome_recursive(text, left, right)
    else:
        return False

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()

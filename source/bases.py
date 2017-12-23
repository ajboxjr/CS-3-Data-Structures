#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # DONE__: Decode digits from binary (base 2)
    # DONE__: Decode digits from any base (2 up to 36)
    # DONE__: Decode digits from hexadecimal (base 16)

    # Sum of places for encoding
    result = 0
    reverse_digit = str(digits)[::-1]

    if base == 16:
        for (index,value) in enumerate(reverse_digit):
            if ord(value) > 64 and ord(value) < 71:
                value = ord(value)-55
            result += (base**index) * int(value)
    else:
        for (index,value) in enumerate(reverse_digit):
            result += (base**index) * int(value)

    print("{}{} == {}{}".format(digits,sub(base), result,sub(10)))
    return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    result = ""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)

    #Whole  is the whole version value of the number
    whole = number

    # Handle unsigned numbers only for now
    # DONE__: Encode number in binary (base 2)
    # DONE: Encode number in any base (2 up to 36)

    if base == 16:
        while whole > 0:
            whole, remainder = divmod(whole, base)
            # If the remainder is greater than 10 use chars A-F
            if remainder >= 10:
                remainder = chr(remainder+55)
            result += str(remainder)
        result = result[::-1]
    else:
        while whole > 0:
            whole, remainder = divmod(whole, base)
            result += str(remainder)
        result = result[::-1]
    # TODO: Encode number in hexadecimal (base 16)

    print("{}{} == {}{}".format(number,sub(10),result,sub(base)))
    return result


def sub(base):
    str_base = str(base)
    subscript = ""
    for char in str_base:
         subscript +=chr(0x2080+int(char))
    return subscript

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # DONE__: Convert digits from base 2 to base 16 (and vice versa)
    # DONE__: Convert digits from base 2 to base 10 (and vice versa)
    # DONE__: Convert digits from base 10 to base 16 (and vice versa)
    # DONE__: Convert digits from any base to any base (2 up to 36)
    result = ""

    result =  encode(decode(digits,base1),base2)
    print("{}{} == {}{}".format(digits,sub(base1), result, sub(base2)))
    return result

    # ...
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

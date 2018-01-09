#!python

import string
import decimal
decimal.getcontext().prec = 3
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


# Return subscript of base
def sub(base):
    str_base = str(base)
    subscript = ""
    for char in str_base:
         subscript +=chr(0x2080+int(char))
    return subscript

"""
In: str 0-9a-Z
out: str base_10
"""
def base_to_ten(value):
    if ord(value) >= 97 and ord(value) <= 102:
        value = ord(value)-87
    return value

"""
In: int base_x
out: int base_10
"""
def ten_to_base(value):
    if value >= 10:
        value = chr(value+87)
    return value

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
    whole = ""
    decimal = ""

    #Radix Numbers(decimal)
    if "." in digits:
        whole, decimal = digits.split(".")
        #Iterate through decimal x^-1_, x^-2
        for (index, value) in enumerate(decimal):
            index= -int(index) - 1
            #determine and convert a values (0-9a-Z) to base 10
            value = base_to_ten(value)
            result += (base ** index) * int(value)
    else:
        whole = str(digits)

    #Whole Numbers
    #Iterate through whole number backwards  x^0_, x^1
    for (index,value) in enumerate(whole[::-1]):
            #For Base 16
            # converting unicode of char to int - 87 ex. a= 97-87=10
            value = base_to_ten(value)
            result += (base ** index) * int(value)

    print("{}{} == {}{}".format(digits,sub(base), result,sub(10)))
    return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    # DONE__: Encode number in binary (base 2)
    # DONE__: Encode number in any base (2 up to 36)
    # Done__: Encode number in hexadecimal (base 16)
    result = ""
    whole = 0
    #Whole  is the whole version value of the number
    remainder = decimal.Decimal(number)-int(number)

    #For repeating numbers add a precision count
    precision_count = 3

    if remainder:
        while remainder  > .01 and len(result) <= precision_count:
            product = remainder*base

            whole, remainder = int(product), product-int(product)
            result += str(ten_to_base(whole))
        result = str(result)[::-1]+"."
        whole = int(number)

    #Whole Numbers
    while whole > 0:
        whole, remainder = divmod(whole, base)
        print(whole, remainder)
        # If the remainder is greater than 10 use chars A-F
        result += str(ten_to_base(remainder))
    result = result[::-1]

    print("{}{} == {}{}".format(number,sub(10),result,sub(base)))
    return result

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

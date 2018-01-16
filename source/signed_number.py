from bases import *
#Twos compliment
#With Decimal

def decimal_to_binary(decimal):
    """Convert decimal to binary
    In: (int) decimal
    Out: (int) binary
    """
    return format(decimal, 'b')

def ones_compliment_decimal(number, bits):
    #Check if the number in binary <= to num of bits
    assert number < 0
    assert len(encode(abs(number),2 )) <= bits

    max_bit = (2 ** bits-1)

    print("unsigned bits 0-{}".format(max_bit))
    return number+max_bit

def twos_compliment_decimal(number,bits):
    return ones_compliment_decimal(number, bits) +1

def ones_compliment_binary(binary):
    """Convert binary two ones compliment
    In: str -- a string of binary numbers
    Out: str -- a integer of ones_compliment"""
    assert len(binary) > 0

    ones_compliment = ""
    for pos in binary:
        if pos == "1":
            ones_compliment += "0"
        else:
            ones_compliment += "1"
    print("ones_compliment: {}".format(ones_compliment))
    return ones_compliment

def twos_compliment_binary(binary):
    """Add one to ones compliment to get Twos ones_compliment
    In: str
    Out: str
    """
    ones_comp = ""
    twos_compliment = ""

    ones_comp = ones_compliment_binary(binary)

    # add one to ones ones_compliment
    carry = 1
    for index in range(len(binary)):
        #Iterate left to right
        val = int(binary[-1-index])
        if val + carry == 0:
            twos_compliment += "0"
        elif val + carry == 1:
            twos_compliment += "1"
            carry = 0
        elif val + carry == 2:
            twos_compliment += "0"
            carry  = 1
    #Reverse the reversed twos_compliment
    return twos_compliment[::-1]





print(twos_compliment_decimal(-95,8))
print(twos_compliment_binary("01011111"))

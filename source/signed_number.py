from bases import *


def digit_to_binary(digit):
    """Convert digit into binary
    In: (int) digit negative or positive
    Out: (str) binary """
    assert type(digit) == int
    binary = format(abs(digit), 'b')
    formatted_binary = format_binary(binary, bit_length_rounded(binary))
    print("{}  => {}{}".format(digit, formatted_binary,sub(2)))
    return formatted_binary
    
def bit_length_rounded(binary):
    """Round bit length up by fours ex. 5 => 2
    In: (str) Binary numbers
    Out: (int) nibbles rounded up by four"""
    bit_length = len(binary)
    whole, remainder = divmod(bit_length, 4)
    if remainder:
        whole +=1
    return whole*4

def format_binary(binary, bits):
    """Return binary at length of bits
    In: (str) Binary Numbers
    Out: (int) bit length"""
    trimmed_bits = bits-len(binary)
    return ("0"*trimmed_bits)+binary

def ones_compliment(binary):
    """Convert binary to ones compliment
    In: (str) binary
    Out: (str) ones compliment inverse"""
    bits = bit_length_rounded(binary)
    return ones_compliment_binary(binary,bits)

def twos_compliment(binary):
    """Convert binary to twos compliment
    In: (str) ones compliment Binary
    Out: (str) two compliment Binary"""
    bits = bit_length_rounded(binary)
    ones_comp = ones_compliment_binary(binary,bits)
    print(ones_comp)
    twos_comp = twos_compliment_binary(ones_comp)
    format_binary(twos_comp, bits)
    return twos_comp

def ones_compliment_binary(binary,bits):
    """Convert binary two ones compliment
    In: str, int -- a string of binary numbers
    Out: str -- a integer of ones_compliment"""
    assert len(binary) > 0
    unsigned_bits = (2 ** bits-1)
    ones_compliment = unsigned_bits- int(binary,2)
    return format(ones_compliment, 'b')

def twos_compliment_binary(binary):
    """Convert binary into twos ones_compliment
    In: (str) binary ones compliment
    Out: (str) binary twos compliment"""
    twos_compliment = format(int(binary,2)+1, 'b')
    return twos_compliment



if __name__ == '__main__':
    binary = digit_to_binary(3)
    print(twos_compliment(binary))
    print(twos_compliment("0011"))

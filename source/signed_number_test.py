gimport unittest
from signed_number import *

class Signed_Numbers_Test(unittest.TestCase):

    def ones_compliment_four_bits(self):
        assert ones_compliment("0000") == "1111"
        assert ones_compliment("1010") == "0101"
        assert ones_compliment("0011") == "1100"
        assert ones_compliment("1100") == "0011"
        assert ones_compliment("0101") == "1010"

    def ones_compliment_eight_bits(self):
        assert ones_compliment("10010010") == "01101101"
        assert ones_compliment("00010010") == "11101101"
        assert ones_compliment("00100110") == "11011001"

    def twos_compliment_four_bits(self):
        assert twos_compliment("1011") == "1100"
        assert twos_compliment("1100") == "0100"
        assert twos_compliment("0000") == "10000"

    def twos_compliment_eight_bits(self):
        assert twos_compliment("10010110") == "1101010"
        assert twos_compliment("00001010") == "11110110"
        assert twos_compliment("10100011") == "1011101"

if __name__ == '__main__':
    unittest.main()

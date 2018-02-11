from circularbuffer import CircularBuffer
from linkedlist import LinkedList
import unittest

class CircularBufferTest(unittest.TestCase):
    def setUp(self):
        self.cb = CircularBuffer(4)

    def test_enqueue(self):
        self.cb.enqueue('one')
        self.cb.enqueue('two')
        self.cb.enqueue('three')
        self.cb.enqueue('four')
        self.cb.enqueue('!!!!')
        #Create a __eq__function
        assert self.cb.get_at_index(0) == '!!!!'

    def test_size(self):
        self.cb.enqueue(101)
        self.cb.enqueue(202)
        self.cb.enqueue(303)
        print(self.cb.size())
        assert self.cb.size() == 3
        self.cb.enqueue(404)
        self.cb.enqueue(505)
        assert self.cb.size() == 4

if __name__ == '__main__':
    unittest.main()

from set import Set
import unittest

class set_test(unittest.TestCase):
    def setUp(self):
        self.set_one = Set()
        self.set_two = Set()

    def test_init(self):
        self.set_one = Set()
        assert self.set_one.size() == 0

    def test_add(self):
        self.set_one.add('fda')
        self.set_one.add(1)
        self.set_one.add(('a','tuple'))
        assert self.set_one.size() == 3
    def test_contains(self):
        self.set_one.add('a')
        self.set_one.add('b')
        self.set_one.add('c')
        assert self.set_one.contains('a') == True
        assert self.set_one.contains('z') == False
    def test_remove(self):
        self.set_one.add('don\'t')
        self.set_one.add('remove')
        self.set_one.add('me')
        self.set_one.add(')')
        self.set_one.add(':')
        self.set_one.add('(')
        self.set_one.size() == 6
        self.set_one.remove('don\'t')
        self.set_one.remove(')')
        self.set_one.size() == 4

    def test_union(self):
        self.set_one = Set([('one'),('two'),('three')])
        self.set_two = Set([('three'),('one'),('five'),('nine')])
        self.set_one.union(self.set_two)
        assert self.set_one.size() == 3

    def test_intersection(self):
        self.set_one = Set([('1'),('3'),('a',43),('a',95),('4',14)])
        self.set_two = Set([('u3'),'1',('3'),('b')])
        #Ints as strings
        self.set_one.intersection(self.set_two) == {1,3}

    def test_diffrence(self):
        self.set_one = Set([('one'),('two'),('three')])
        self.set_two = Set([('three'),('one'),('five'),('nine')])
        self.set_one.difference(self.set_two) == {'two','five','nine'}

    def test_is_subset(self):
        self.set_one = Set(['one','grandpa','two','children'])
        self.set_two = Set(['grandma','children','three','five'])
        self.set_three = Set(['one','grandpa'])
        assert self.set_one.is_subset(self.set_two) == False
        assert self.set_one.is_subset(self.set_three) == True


if __name__ == '__main__':
    unittest.main()

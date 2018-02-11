from hashtable import HashTable

# TODO: make set a hashtable
class Set(object):
    def __init__(self,items=0):
        self._set = HashTable()
        if items:
            for element in items:
                self.add(element)
    def __repr__(self):
        """Return string representation of elements
        Time Complexity Worst: 0(N), n elements  Best: Ω(1) 0-1 element"""
        items = []
        for element in self._set.keys():
            items.append(str(element))
        return '{' + ','.join(items) + '}'

        return self._set.keys()
    def size(self):
        """Return size of set
        Time Complexity Worst: 0(N), n elements  Best: Ω(1) 0-1 element"""
        return len(self._set.keys())

    def contains(self,element):
        """Return True if element is in set, False if not
        Time Complexity Worst: 0(N)-linearprobe O(?)-Quadratic Probe O(?) Double Hash 0(?)-Linear Probing,
        Best: Ω(1), Contained in first buket of HashTable"""
        return self._set.contains(element)

    def add(self,element):
        """Add new element to set
        Time Complexity Worst: 0(?)  Best: Ω(?)"""
        self._set.set(element,None)

    def remove(self,element):
        """Remove element from set
        Time Complexity Worst: 0(?)  Best: Ω(?)"""
        self._set.delete(element)

    def union(self,other_set):
        """Return new set of all elements
        Time Complexity Worst: 0(?)  Best: Ω(?)"""
        assert type(other_set) == Set
        # assert type(other_set) == 'Set'
        new_set = Set(self._set.keys()+other_set._set.keys())
        # for element in other_set._set.keys():
        #     new_set.add(element)
        return new_set
        
    def intersection(self,other_set):
        """Return new set of elements contained in both sets
        Time Complexity Worst: 0(?)  Best: Ω(?)"""
        assert type(other_set) == Set
        new_set = Set()
        for element in other_set._set.keys():
            if self._set.contains(element) is True:
                new_set.add(element)
        return new_set

    def difference(self,other_set):
        """Return new set of elements unique to both sets
        Time Complexity Worst: 0(?)  Best: Ω(?)"""
        assert type(other_set) == Set

        new_set = Set()
        for element in other_set._set.keys():
            if self._set.contains(element) is False:
                new_set.add(element)
        return new_set

    def is_subset(self,other_set):
        """Return whether other set is a subset(contains all elements) of set
        Time Complexity Worst: 0(?)  Best: Ω(?)"""
        assert type(other_set) == Set
        for element in other_set._set.keys():
            if self._set.contains(element) is False:
                return False
        return True

if __name__ == '__main__':
    h = Set([('a',3),('3',133),('k',43),('y',95),('4',14)])
    z = Set([('u',3),('3',12),('1',43),('90',95),('b',14)])
    print(h.union(z))
    m = Set()
    m.add(('3', 133))
    print(m)

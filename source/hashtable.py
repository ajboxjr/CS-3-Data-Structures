#!python
import math
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())
    def __setitem__(self, key, value):
        """ A[key]= value notation"""
        self.set(key,value)
    def __getitem__(self,key):
        """ return value using A[key] notation """
        return self.get(key)
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Worst Bucket O(N) N Buckets
        Best Ω(1) one bucket"""
        # TODO: Calculate load factor
        return self.size/len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Worst: 0(N*M) N=buckets M=items in bucket
        Best: O(N)(1=Bucket, M keys) or (N=Buckets, 1 Item)"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets: #O(N)
            for key, value in bucket.items(): #O(M)
                all_keys.append(key) #O(1)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Worst: 0(N*M) N=buckets M=items in bucket
        Best O(N)(1=Bucket, M value) or (N=Buckets, 1 Item)"""
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Worst: O(N*M) N buckets M items
        Best: Ω(N) one bucket M items """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets: #O(N)
            all_items.extend(bucket.items()) #O(M)
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Worst: O(N*M) N Buckets and M Items in the bucket
        Best: Ω(N) 1 Bucket and M items"""
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets: #O(N)
            item_count += bucket.length() #(M) items
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: Ω(N)  [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key) #O(1)

        #Seperate Chaining
        # bucket = self.buckets[index]

        #Linear Probe
        # bucket =  self.linear_probe(key,index)

        #Quadratic Probe
        # bucket = self.quadradic_probe(key,index)

        #Double Hash probe
        bucket = self.double_hashing_probe(key,index)

        entry = bucket.find(lambda key_value: key_value[0] == key) #0(k)


        # # Check if an entry with the given key exists in that bucket
        return entry is not None  # True or False #0(1)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)

    # Find the entry with the given key in that bucket, if one exists
        #Seperate Chaining
        #bucket = self.buckets[index]

        #Linear Probing
        #bucket= self.linear_probe(key,index)

        #Quadratic Probing
        # bucket = self.quadradic_probe(key,index)

        #Double Hash Probing
        bucket = self.double_hashing_probe(key,index)

        entry = bucket.find(lambda key_value: key_value[0] == key)

        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def linear_probe(self,key,index):
        """Return the bucket with the respective key or first bucket if (Not Present)"""
        for i in range(0,len(self.buckets)-1):
            bucket = self.buckets[(index+i)%len(self.buckets)]
            entry = bucket.find(lambda key_value: key_value[0] == key)
            if entry is not None:
                return bucket
        return bucket

    def quadradic_probe(self,key,index,i=0):
        """Return the bucket with respective key or first bucket if (Not Present)"""
        if i < 13:
            bucket = self.buckets[(index+(i**2))%len(self.buckets)]
            entry = bucket.find(lambda key_value: key_value[0] == key)
            if entry is not None:
                return bucket
            else:
                i+=1
                self.quadradic_probe(key,index,i)
        return self.buckets[index]

    def isPrime(self,num):
        # print(num)
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # TODO: Set on init and on resize
    def get_prime(self,value):
        if self.isPrime(value):
            return value
        return self.get_prime(value-1)

    def _prime_hash(self, key):
        prime = self.get_prime(len(self.buckets))
        return prime-(hash(key)%prime)

    def double_hashing_probe(self,key,index):
        hash_two = self._prime_hash(key)
        for i in range(0,len(self.buckets)-1):
            bucket = self.buckets[(index+(i*hash_two))%len(self.buckets)]
            entry = bucket.find(lambda key_value: key_value[0] == key)
            if bucket.length() > 0: # not empty
                if entry is not None: #found key
                    return bucket # return found bucket
                else:
                    pass #keep iterating
        return bucket #return empty buckt



    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)

    # Find the entry with the given key in that bucket, if one exists
    # Check if an entry with the given key exists in that bucket

        #Seperate Chaining
        # bucket = self.buckets[index]

        # Linear Probing
        # bucket = self.linear_probe_set(key, index)

        #Quadratic Probing
        # bucket = self.quadradic_probe_set(key,index,value)

        #Double Hash Probing
        bucket = self.double_hashing_set(key,index)

        entry = bucket.find(lambda key_value: key_value[0] == key)

        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
        # Insert the new key-value entry into the bucket in either case
        else:
            self.size +=1

        bucket.append((key,value))
        # Check if the load factor exceeds a threshold such as 0.75
        # If so, automatically resize to reduce the load factor
        if self.load_factor() > .75:
            print('resizing load factor')
            self._resize()

    def linear_probe_set(self, key,index):
        """Return bucket containing key or a empty bucket"""
        for i in range(0,len(self.buckets)-1):
            # print("probe index ",(index+i)%len(self.buckets))
            bucket = self.buckets[(index+i)%len(self.buckets)]
            #if key is in bucket delete and add new
            if bucket.length() != 0: #if has a value
                entry = bucket.find(lambda key_value: key_value[0] == key)
                if entry is not None: # if key found
                    return bucket
            else: #if key empty
                #Return None (empty Bucket)
                return bucket

    def quadradic_probe_set(self,key,index,value, i=0):
        new_index = (index+(i**2))%len(self.buckets)
        bucket = self.buckets[new_index]
        if bucket.length != 0:
            entry = bucket.find(lambda key_value: key_value[0] == key)
            if entry is not None: #Found
                return bucket
            else:
                i+=1
                self.quadradic_probe(key,index,i)
        # else: #If Empty
        return bucket

    def double_hashing_set(self,key,index):
        hash_two = self._prime_hash(key)
        for i in range(0,len(self.buckets)-1):
            bucket = self.buckets[(index+(i*hash_two))%len(self.buckets)]
            entry = bucket.find(lambda key_value: key_value[0] == key)
            if bucket.length() > 0: # not empty
                if entry is not None: #found key
                    return bucket # return found bucket
                # else:
                #     pass #keep iterating
            else: #empty
                return bucket #return empty bucket
        #trigger resize and call again
        print('resize??')
        self._resize()
        return self.double_hashing_set(key,index)

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time:  under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
    # Find the entry with the given key in that bucket, if one exists

        #Seperate Chaining
        #bucket = self.buckets[index]

        #Linear Probing
        # bucket = self.linear_probe(key,index)

        #Quadratic Probing
        # bucket = self.quadradic_probe(key,index)

        #Double Hash Probing
        bucket = self.double_hashing_probe(key,index)

        entry = bucket.find(lambda key_value: key_value[0] == key)

        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -=1
            #Setting Load factor to delete extra entries
            if self.load_factor() < 1:
                print('resizing load factor')
                self._resize(0)
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: ??? under what conditions? [TODO]
        Best and worst case space usage: ??? what uses this memory? [TODO]"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = int(len(self.buckets) / 2)  # Half size
        # TODO: Get a list to temporarily hold all current key-value entries
        temp_items = self.items()
        # TODO: Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for _ in range(new_size)]
        self.size = 0
        # TODO: Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for (key,value) in temp_items:
            self.set(key,value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    ht.set('M', 5)
    print('set(M, 5): ' + str(ht))
    ht.set('R', 5)
    print('set(R, 5): ' + str(ht))
    ht.set('C', 5)
    print('set(C, 5): ' + str(ht))
    ht.set('L', 5)
    print('set(L, 5): ' + str(ht))
    ht.set('K', 5)
    print('set(K, 5): ' + str(ht))
    ht.set('Y', 5)
    print('set(Y, 5): ' + str(ht))


    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()

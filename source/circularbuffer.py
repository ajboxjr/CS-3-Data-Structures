from linkedlist import LinkedList

class CircularBuffer(object):
    def __init__(self,max_size=4):
        self.ll = LinkedList()
        self.max_size = max_size
        self.counter = 0
        self.start_pointer = 0
        self.end_pointer = 0
        for _ in range(max_size):
            self.ll.append(None)

    def __repr__(self):
        return self.ll.__str__()
    #
    # def __str___(self):
    #     return self.ll.__str__()

    def size(self):
        count = 0
        for node in self.ll:
            if node.data is not None:
                count +=1
        return count
    def get_at_index(self,index):
        return self.ll.get_at_index(index)

    def is_empty(self):
        for node in self.ll:
            if node.data is not None:
                return False
        return True

    def is_full(self):
        for node in self.ll:
            if node.data is None:
                return False
        return True

    def move_pointer(self,pointer):
        # if self.is_full():
        #     if self.start_pointer == self.end_pointer:
        #         self.end_pointer +=1
        # end on write checks
        #if end == start report end of buffer
        #if
        if pointer == 'start':
            self.counter += 1
            self.start_pointer = self.counter%self.max_size
            # if self.start_pointer == self.max_size:
            #     self.start_pointer = 0
            print("start: {}, end:{}".format(self.start_pointer, self.end_pointer))
        # if pointer == 'end':
        #     if self.end_pointer == self.max_size:
        #         self.end_pointer = 0

    def front(self):
        if self.is_empty() is False:
            read = self.get_at_index(self.end_pointer)
            self.move_pointer('end')
        return read

    def enqueue(self,item):
        if self.is_full() is False:
            self.ll.insert_at_index(self.start_pointer,item)
            self.move_pointer('start')
        else:
            self.ll.insert_at_index(self.start_pointer,item)
            self.move_pointer('start')
        print(self.ll)

            # if self.start_pointer

if __name__ == '__main__':
    cb = CircularBuffer()
    print(cb)
    cb.enqueue('hi')
    cb.enqueue('hi')
    cb.enqueue('hi')
    cb.enqueue('hi')
    cb.enqueue('bye')
    print(cb)
    print(cb.size())

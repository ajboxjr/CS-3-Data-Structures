from linkedlist import LinkedList

class CircularBuffer(object):
    def __init__(self,max_size=4):
        self.ll = LinkedList()
        self.max_size = max_size
        self.start_pointer = 0
        self.end_pointer = 0
        # for _ in range(max_size):
        #     self.ll.append(None)

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
        return  self.ll.size < self.max_size
        # for node in self.ll:
        #     if node.data is not None:
        #         return False
        # return True

    def is_full(self):
        return self.ll.size == self.max_size

    def move_pointer(self,pointer):
        if pointer == 'start':
            self.start_pointer += 1
        if pointer == 'end':
            self.end_pointer += 1


    def front(self):

        # print("start: {}, end:{}".format(self.get_start_index(), self.get_end_pointer()))
        if self.start_pointer != self.end_pointer:
            read = self.get_at_index(self.get_end_pointer())
            self.move_pointer('end')
            return read
        else:
            pass

    def get_start_index(self):
        return self.start_pointer%self.max_size

    def get_end_pointer(self):
        return self.end_pointer%self.max_size

    def enqueue(self,item):
        #If the buffer is not full, write to empty spaces
        #if full overwrite buffer data
        if self.is_empty() is True:
            self.ll.append(item)
        elif self.is_full() is True:
            self.ll.replace_at_index(self.get_start_index(),item)
        print(self.get_start_index())
        self.move_pointer('start')

            # if self.start_pointer

if __name__ == '__main__':
    cb = CircularBuffer()
    print(cb)
    cb.enqueue('one')
    cb.enqueue('two')
    cb.enqueue('three')
    cb.enqueue('four')
    cb.enqueue('five')
    cb.enqueue('six')
    print(cb)
    print(cb.size())

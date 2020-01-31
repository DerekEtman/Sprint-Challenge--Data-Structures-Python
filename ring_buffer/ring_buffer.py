from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Problem: We want a FIFO set up, add items until capacity is full. if full - remove first element and replace.
        # if the buffer is full delete the node its on top of
        # add to the tail, this constantly shifts the head of the ring buffer over
        # ex: h = head of ring [ h*1,2,3,4] -> [5, h*2,3,4] -> [5,6,h*3,4] -> 

        # if current is larger than capacity
        # tracking current size of ring
        size_tracker = 0

        # Checking to see if ring is at max capacity.
        if size_tracker > self.capacity:
            # delete current 
            self.storage.delete(self.current)
            size_tracker -= 1
            # add item to tail
            self.storage.add_to_tail(item)
            size_tracker += 1

        # if size_tracker < self.capacity:
        #     self.current = item
        #     self.storage.add_to_tail(self.current)
        #     size_tracker += 1

        self.storage.add_to_tail(item)
        # self.current = (size_tracker + 1) % self.capacity
        print(f"Size Tracker: {size_tracker}, current item: {item}")


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

    
        if len(list_buffer_contents) < self.capacity:
            # list_buffer_contents.append(self.current)
            list_buffer_contents.append(self.current)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

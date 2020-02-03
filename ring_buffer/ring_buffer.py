from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size_tracker = 0

    def append(self, item):
        # Problem: We want a FIFO set up, add items until capacity is full. if full - remove first element and replace.
        # if the buffer is full delete the node its on top of
        # add to the tail, this constantly shifts the head of the ring buffer over
        # ex: h = head of ring [ h*1,2,3,4] -> [5, h*2,3,4] -> [5,6,h*3,4] -> 

        # if current is larger than capacity
        # tracking current size of ring

        # Checking to see if ring is at max capacity.

        if self.size_tracker < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            self.size_tracker += 1

        
        if self.size_tracker == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        # print(f"storage head: {self.storage.head.value}, adding item {item}")
        # print(f"self.current: {self.current}")


    def get(self):
        # Note:  This is the only [] allowed
   
        # if self.current:
        #     list_buffer_contents.append(self.current.value)
        #     # Keep repeating, updating self.current with the next value
        #     while self.current.next:
        #         self.current = self.current.next
        #         list_buffer_contents.append(self.current.value)
        # compare that we have the same amount of elements in our list vs storage

        # if len(list_buffer_contents) < self.storage.length:

        list_buffer_contents = []
        element = self.storage.head

        while element:
          list_buffer_contents.append(element.value)
          element = element.next

        return list_buffer_contents



# ______________________ old code _________________________


        # If there is a current object: add it to the list
        # if self.current:
        #     list_buffer_contents.append(self.current.value)
        #     # Keep repeating, updating self.current with the next value
        #     while self.current.next:
        #         self.current = self.current.next
        #         list_buffer_contents.append(self.current.value)
        # # compare that we have the same amount of elements in our list vs storage
        # if len(list_buffer_contents) < self.storage.length:
        #   element = self.storage.head
        #   list_buffer_contents.append(element.value)
        #   while element.next and len(list_buffer_contents) < self.storage.length:
        #     element = element.next
        #     list_buffer_contents.append(element.value)


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.size += 1
        print(value)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            print("0")
            return None
        else:
            self.size -= 1
            value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.storage.length

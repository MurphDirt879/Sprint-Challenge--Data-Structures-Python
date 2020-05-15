from doublyLinkedList import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.firstIn = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            if self.storage.length == 1:
                self.firstIn = self.storage.head

        else:
            self.firstIn.value = item
            if self.firstIn != self.storage.tail:
                self.firstIn = self.firstIn.next
            else:
                self.firstIn = self.storage.head

    def get(self):
        ringBufferList = []
        node = self.storage.head
        while node  != None:
            ringBufferList.append(node.value)
            node = node.next
        return ringBufferList
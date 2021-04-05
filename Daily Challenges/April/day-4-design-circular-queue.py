class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.sizeOfQueue = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.sizeOfQueue += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.sizeOfQueue -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        if self.sizeOfQueue == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.sizeOfQueue == self.size:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

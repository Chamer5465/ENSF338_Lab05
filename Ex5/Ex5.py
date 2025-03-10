# ex5.py


#1
class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity  
        self.front = 0  
        self.count = 0  

    def enqueue(self, item):
        if self.count == self.capacity:
            print("enqueue None")
            return

        rear = (self.front + self.count) % self.capacity
        self.queue[rear] = item
        self.count += 1
        print("enqueue :", item)

    def dequeue(self):
        if self.count == 0:
            print("dequeue None")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None  
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print("dequeue :", item)
        return item

    def peek(self):
        if self.count == 0:
            print("peek None")
            return None
        item = self.queue[self.front]
        print("peek :", item)
        return item

#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.tail = None 

    def enqueue(self, item):
        if self.count == self.capacity:
            print("enqueue None")
            return
        new_node = Node(item)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next  
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        print("enqueue :", item)

    def dequeue(self):
        if self.count == 0:
            print("dequeue None")
            return None
        head = self.tail.next
        if self.count == 1:
            self.tail = None
        else:
            self.tail.next = head.next
        self.count -= 1
        print("dequeue :", head.data)
        return head.data

    def peek(self):
        if self.count == 0:
            print("peek None")
            return None
        head = self.tail.next
        print("peek :", head.data)
        return head.data

#3
def test_queue(myList):
    myList.peek()
    myList.dequeue()
    myList.enqueue(1)
    myList.enqueue(2)
    myList.enqueue(3)
    myList.peek()
    myList.dequeue()
    myList.enqueue(4)
    myList.enqueue(5)
    myList.enqueue(6)
    myList.enqueue(7)
    myList.peek()
    myList.dequeue()
    myList.dequeue()
    myList.peek()
    myList.enqueue(7)
    myList.enqueue(8)
    myList.enqueue(9)
    myList.enqueue(10)
    myList.dequeue()
    myList.dequeue()
    myList.dequeue()
    myList.dequeue()
    myList.peek()
    myList.dequeue()
    myList.dequeue()
    myList.dequeue()
    myList.peek()
    myList.enqueue(11)
    myList.enqueue(12)
    myList.enqueue(13)
    myList.enqueue(14)
    myList.dequeue()
    myList.enqueue(15)
    myList.peek()
    myList.enqueue(16)
    myList.enqueue(17)
    myList.dequeue()
    myList.dequeue()
    myList.peek()


def main():
    print("Testing Circular Queue Array:")
    circular_array = CircularQueueArray(5)
    test_queue(circular_array)
    
    print("Testing Circular Queue Linked List:")
    circular_linked = CircularQueueLinkedList(5)
    test_queue(circular_linked)

if __name__ == '__main__':
    main()
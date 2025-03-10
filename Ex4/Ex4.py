import random
import timeit
import matplotlib.pyplot as plt
import numpy as np


class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None  
        self.tail = None  
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    

    def dequeue(self):
        if self.tail is None:
            return None
        
        if self.head == self.tail:
            result = self.tail.data
            self.head = None
            self.tail = None
            return result
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        result = self.tail.data
        current.next = None
        self.tail = current
        return result


def generate_tasks(n):
    tasks = []
    for i in range(n):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 100)))
        else:
            tasks.append(('dequeue', None))
    return tasks


def run_linkedlist_tasks(tasks):
    queu = LinkedListQueue()
    for i, value in tasks:
        if i == 'enqueue':
            queu.enqueue(value)
        else:
            queu.dequeue()

def run_array_tasks(tasks):
    queu = ArrayQueue()
    for i, value in tasks:
        if i == 'enqueue':
            queu.enqueue(value)
        else:
            queu.dequeue()


def measure_arrayqueue(tasks_lists):
    times = []
    for tasks in tasks_lists:
        def time():
            run_array_tasks(tasks)
        t = timeit.timeit(time, number=1)
        times.append(t)
    return times

def measure_linkedlistqueue(tasks_lists):
    times = []
    for tasks in tasks_lists:
        def time():
            run_linkedlist_tasks(tasks)
        t = timeit.timeit(time, number=1)
        times.append(t)
    return times


def main():
    num_lists = 100
    tasks_lists = [generate_tasks(10000) for _ in range(num_lists)]
    
    array_time_list = measure_arrayqueue(tasks_lists)
    linkedlist_time_list = measure_linkedlistqueue(tasks_lists)
    
    array_time_sorted = np.sort(array_time_list)
    linkedlist_time_sorted = np.sort(linkedlist_time_list)

    plt.figure(figsize=(10, 5))
    plt.plot(array_time_sorted, marker='o', label='ArrayQueue')
    plt.plot(linkedlist_time_sorted, marker='o', label='LinkedListQueue')
    plt.xlabel('Sorted Sample')
    plt.ylabel('Execution Time')
    plt.title('Distribution of Execution Times')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

    # Question 5 discussion
    #  ArrayListQueue is consistently out performing LinkedListQueue.
    #  From the slight peak on the right side we see that under poor circumstances the performance of the linked list is impacted compared to the much flatter graph for ArrayListQueue.
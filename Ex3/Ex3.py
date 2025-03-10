import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

class Array:
    def __init__(self, data=[]):
        self.array = data

    def display(self):
        print(self.array)

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if not self.array:
            return None
        return self.array.pop()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self
        return new_node

    def pop(self):
        if self is None or self.next is None:
            return None, None
        return self.next, self.data

    def displayLL(self):
        current = self
        while current:
            print(current.data)
            current = current.next

# similar function in ex 2 of this lab
def generate_task_list(size=10000):
    return ["push" if random.random() < 0.7 else "pop" for _ in range(size)]


def run_tasks(data_structure, tasks):
    for task in tasks:
        if task == "push":
            data_structure.push(random.randint(1, 100))
        else:
            data_structure.pop()

# most of this is taken from lab 4
def measure_performance():
    sizes = [1000, 2000, 4000, 8000, 16000, 32000]
    trialRun = 10
    array_times = []
    linked_list_times = []

    for size in sizes:
        tasks = generate_task_list(size)

        array = Array()
        array_time = timeit.timeit(lambda: run_tasks(array, tasks), number=trialRun)
        linked_list = Node(0)
        linked_list_time = timeit.timeit(lambda: run_tasks(linked_list, tasks), number=trialRun)

        print(f"Array time for {size} tasks: {array_time:.6f} seconds")
        print(f"Linked list time for {size} tasks: {linked_list_time:.6f} seconds")

        array_times.append(array_time)
        linked_list_times.append(linked_list_time)

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, array_times, marker='o', label='Array Implementation', color='red')
    plt.plot(sizes, linked_list_times, marker='x', label='Linked List Implementation', color='blue')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Performance Comparison of Array vs Linked List Implementations')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    measure_performance()

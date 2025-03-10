import random
import timeit

class PriorityQueueMergeSort:
    def __init__(self):
        self.queue = []

    # this is taken from lab 3 submission
    def merge(arr, low, mid, high):
        n1 = mid - low + 1
        n2 = high - mid
        
        L = [0] * n1
        H = [0] * n2
        
        for i in range(n1):
            L[i] = arr[low + i]
        for j in range(n2):
            H[j] = arr[mid + 1 + j]
        
        i, j, k = 0, 0, low
        
        while i < n1 and j < n2:
            if L[i] <= H[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = H[j]
                j += 1
            k += 1
        
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < n2:
            arr[k] = H[j]
            j += 1
            k += 1

    # this was implemented because traditional mergesort takes WAY too long
    # upwards of 10+ mins for each test now it works similarly to insert
    def incremental_mergesort(self):
        """
        rather than do a merge sort on everything again each enqueue just merge sort the 
        newest part
        """
        n = len(self.queue)
        if n <= 1:
            return
        PriorityQueueMergeSort.merge(self.queue, 0, n-2, n-1)

    def enqueue(self, value):
        self.queue.append(value)
        self.incremental_mergesort()

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        if not self.queue:
            self.queue.append(value)
            return
        for i in range(len(self.queue)):
            if value < self.queue[i]:
                self.queue.insert(i, value)
                return
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

#generate a list of tasks with a corresponding item to enqueue or dequeue
def generate_task_lists(n=100):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 1000)))
        else:
            tasks.append(("dequeue", None))
    return tasks

#Operate based on the generated task list
def test_performance(queue_class, task_lists):
    def run():
        pq = queue_class()
        for tasks in task_lists:
            for action, value in tasks:
                if action == "enqueue":
                    pq.enqueue(value)
                else:
                    pq.dequeue()
    return timeit.timeit(lambda:run, number=10)

def main():
    task_lists = [generate_task_lists() for _ in range(100)]

    time_mergesort = test_performance(PriorityQueueMergeSort, task_lists)
    time_sorted_insert = test_performance(PriorityQueueSortedInsert, task_lists)

    print(f"PriorityQueueMergeSort time: {time_mergesort:.5f} seconds")
    print(f"PriorityQueueSortedInsert time: {time_sorted_insert:.5f} seconds")

if __name__ == "__main__":
    main()



# Question 5
# Insert is much faster than merge. Using the implemenation of the incremented merge sort
# each merge sort call is O(n) complexity rather than a O(nlogn) but as a whole it operates 
# on a O(n*n) due to enqueue. Where as insert only operates on a O(n) at all times 

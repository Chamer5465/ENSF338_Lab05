from sys import argv

class Operation:
    def __init__(self, operator, num1, num2):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2
    
    def calc(self):
        return eval(self.num1 + self.operator + self.num2)
        

class Node:
    def __init__(self, operation):
        self.data = operation
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data

    def peek(self):
        return self.head.data
    

def main():
    stack = Stack()
    data = argv[1]
    indexes = []
    result = Stack()
    '''(- (* 1 3) (/ 6 (+ 1 2)))'''
    for j, e in enumerate(data):
        if e == ')':
            end_index = j
            for i in range(end_index, -1, -1):
                if data[i] == '(' and i not in indexes:
                    start_index = i
                    indexes.append(i)
                    break
            result.push(data[start_index + 1: end_index])
    print(result)





if __name__ == '__main__':
    main()
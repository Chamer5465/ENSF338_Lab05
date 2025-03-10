from sys import argv
        
class Node:
    def __init__(self, operation):
        self.data = operation
        self.result = 0
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return temp.data, temp.result

    def peek(self):
        if self.head == None:
            return None
        return self.head.data
    
    def calc(self):
        if self.head.data.isdigit():
            self.head.result = int(self.head.data)
        else:
            while (True):
                p = self.head
                if '(' not in p.data:
                    if p.data[1] == '-' and p.data[3] == '-':
                        p.result = do_op(p.data[0], int(p.data[1:3]), int(p.data[3:5]))
                    elif p.data[1] == '-':
                        p.result = do_op(p.data[0], int(p.data[1:3]), int(p.data[3]))
                    elif p.data[2] == '-':
                        p.result = do_op(p.data[0], int(p.data[1]), int(p.data[2:4]))            
                    else:
                        p.result = do_op(p.data[0], int(p.data[1]), int(p.data[2]))
                    if p.next != None:
                        q = p.next
                        while (True):
                            if p.data in q.data:
                                q.data = q.data.replace('(' + p.data + ')' , str(p.result))
                            if q.next != None:
                                q = q.next
                            else:
                                break
                if p.next != None:
                    self.pop()
                else:
                    break
            
def do_op(opp, num1, num2):
    match opp:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2

def main():
    data = argv[1].replace(' ', '')
    indexes = []
    stack = Stack()
    temp_stack = Stack()
    if '(' not in data:
        result = (data, int(data))
    else:
        for j, e in enumerate(data):
            if e == ')':
                end_index = j
                for i in range(end_index, -1, -1):
                    if data[i] == '(' and i not in indexes:
                        start_index = i
                        indexes.append(i)
                        break
                temp_stack.push(data[start_index + 1: end_index])
        while True:
            if temp_stack.peek() == None:
                break
            else:
                stack.push(temp_stack.pop()[0])
        stack.calc()
        result = stack.pop()
    print(f'{argv[1]} = {result[1]}')





if __name__ == '__main__':
    main()
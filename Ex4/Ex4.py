import array
class Array:
    def __init__(self,data=[]):
        self.array=data

    def display(self):
        print(self.array)
            
    def push(self,data):
        self.array.append(data)


    def pop(self):
        if len(self.array)<=1:
            self.array=[]
            return None
        self.array.remove(self.array[len(self.array)-1])
        return self.array[len(self.array)-1]
      
        

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self
        self = new_node
        return new_node 
    
    def pop(self):

        if self.next is None:
            return None, None
        return self.next, self.data

    def displayLL(self):
        if (self.next is None):
            print("No data")
            return
        currentNode = self
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
        


    

def main():
    predef=[2,3,5,2,6,7,4]
    arr= Array(predef)
    arr.push(9)
    arr.display()
    print(arr.pop())
    arr.display()
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())

    node = Node(3)
    node = node.push(4)
    node = node.push(5)
    node = node.push(6)
    node.displayLL()
    print("---------")
    node,data = node.pop()
    print(data)
    print("---------")
    node.displayLL()
    print("---------")
    node,data = node.pop()
    node,data = node.pop()
    node,data = node.pop()
    node,data = node.pop()
    node,data = node.pop()
    print("---------")
    node.displayLL()







if __name__ == '__main__':
    main()
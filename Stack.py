class Stack:
    def __init__(self):
        self.stack = []
        self.Size = 0

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        return self.stack[len(self.stack)-1]
    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []
    def getMin(self):
        return min(self.stack)

    def printStack(self):
        if(self.size()==0):
            print("Stack is empty")
        for val in self.stack:
            print(str(val) + "->",end="")
        print()


myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.printStack()
myStack.pop()
print(myStack.size())
print(myStack.getMin())
myStack.clear()
myStack.printStack()





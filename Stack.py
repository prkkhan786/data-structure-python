class Stack:
    def __init__(self):
        self.stack = []
        self.Size = 0

    def push(self,val):
        """
        insert value in stack
        :param val:
        """
        self.stack.append(val)

    def pop(self):
        '''
        Remove element from stack
        :return:
        element removed
        '''
        self.stack.pop()

    def isEmpty(self):
        '''
        checks if stack empty or not
        :return:
        boolean
        '''
        return len(self.stack) == 0
    def peek(self):
        '''
        get the last inserted element in stack
        :return:
        '''
        return self.stack[len(self.stack)-1]
    def size(self):
        '''
        return the size of stack
        :return:
        '''
        return len(self.stack)

    def clear(self):
        '''
        empty the stack
        :return:
        '''
        self.stack = []
    def getMin(self):
        '''
        returns the min element from the stack
        :return:
        '''
        return min(self.stack)

    def printStack(self):
        '''
        print the stack elements
        :return:
        '''
        if(self.size()==0):
            print("Stack is empty")
        for val in self.stack:
            print(str(val) + "->",end="")
        print()

    def isParanthesisBalanced(self,str):
        '''
        checks if the given string has balanced paranthesis
        :return:
        boolean
        '''
        stack = Stack()
        for ch in str:
            if(ch=='{' or ch=='[' or ch=='('):
                stack.push(ch)
            else:
                if(stack.size()==0):
                    return False
                if(ch==']' and stack.peek()=='['):
                    stack.pop()
                elif(ch=='}' and stack.peek()=='{'):
                    stack.pop()
                elif(ch==')' and stack.peek()=='('):
                    stack.pop()
        if(stack.size()==0):
            return True
        else:
            return False



st =Stack()

val = st.isParanthesisBalanced("{}}}")
print(val)
















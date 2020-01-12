class Stack:
    def __init__(self):
        self.stack = []
        self.Size = 0

    def push(self,val):
        """
        O(1)
        insert value in stack
        :param val:
        """
        self.stack.append(val)

    def pop(self):
        '''
        O(1)
        Remove element from stack
        :return:
        element removed
        '''
        self.stack.pop()

    def isEmpty(self):
        '''
        O(1)
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
        return self.stack[-1]
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


    def StockSpanProblem(self,arr):

        '''
        O(n) space
        O(n) time
        :param arr:
        :return:
        '''
        ans = [0] * len(arr)
        ans[0] = 1

        stack = []
        stack.append(0)

        for index in range(1,len(arr)):
            #compate arr[stack.peek()] and arr[index]
            while(len(stack)>0  and arr[stack[-1]<=arr[index]]):
                stack.pop()
            if(len(stack)==0):
                ans[index] = index + 1
            else:
                ans[index] = index - stack[-1]
            stack.append(index)
        return ans


    def NextGreaterElement(self,arr):

        pass

    def hasDuplicateBrackets(self,src):
        '''
        find if there is duplicates brackets or not
        :param src:
        :return:
        '''
        stack = Stack()
        for ch in src:
            if(ch==')'):
                if (stack.peek() == '('):
                    return True
                while (stack.peek() != '('):
                    stack.pop()
                stack.pop()
            else:
                stack.push(ch)

        return False

st = Stack()
ans = st.hasDuplicateBrackets("(((a+(b))+(c+d)))")
print(ans)



























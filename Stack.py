class Stack:
    def __init__(self):
        self.stack = []
        self.Size = 0

    def push(self, val):
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
        return self.stack.pop()

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
        if (len(self.stack) != 0):
            return self.stack[-1]
        print("Stack is empty")

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
        if (self.size() == 0):
            print("Stack is empty")
        for val in self.stack:
            print(str(val) + "->", end="")
        print()

    def isParanthesisBalanced(self, str):
        '''
        checks if the given string has balanced paranthesis
        :return:
        boolean
        '''
        stack = Stack()
        for ch in str:
            if (ch == '{' or ch == '[' or ch == '('):
                stack.push(ch)
            else:
                if (stack.size() == 0):
                    return False
                if (ch == ']' and stack.peek() == '['):
                    stack.pop()
                elif (ch == '}' and stack.peek() == '{'):
                    stack.pop()
                elif (ch == ')' and stack.peek() == '('):
                    stack.pop()
        if (stack.size() == 0):
            return True
        else:
            return False

    def StockSpanProblem(self, arr):

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

        for index in range(1, len(arr)):
            # compate arr[stack.peek()] and arr[index]
            while (len(stack) > 0 and arr[stack[-1] <= arr[index]]):
                stack.pop()
            if (len(stack) == 0):
                ans[index] = index + 1
            else:
                ans[index] = index - stack[-1]
            stack.append(index)
        return ans

    def NextGreaterElement(self, arr):

        '''
        This function finds the next greater element of each element in the array
        :param arr:
        :return:
        '''

        stack = Stack()
        ans = [None] * len(arr)
        stack.push(0)
        for i in range(1, len(arr)):
            while (stack.isEmpty() == False and arr[i] > arr[stack.peek()]):
                val = stack.pop()
                ans[val] = arr[i]
            stack.push(i)

        while (stack.isEmpty() == False):
            ans[stack.pop()] = -1
        return ans

    def hasDuplicateBrackets(self, src):
        '''
        find if there is duplicates brackets or not
        :param src:
        :return:
        '''
        stack = Stack()
        for ch in src:
            if (ch == ')'):
                if (stack.peek() == '('):
                    return True
                while (stack.peek() != '('):
                    stack.pop()
                stack.pop()
            else:
                stack.push(ch)

        return False




def reverseAStringUsingStack(str):
    '''
    Reverse a string using stack data structure
    :param str:
    string to reverse
    :return:
    reversed string
    '''
    st = Stack()

    for ch in str:
        st.push(ch)

    ans = ""
    for _ in range(st.size()):
        ans+= st.pop()

    print(ans)




# st = Stack()
#
# ans = st.NextGreaterElement([5,9,8,3,2,7,16,4,14,19,3])
#
#
# for i in range(10):
#     print(i)


def NextGreaterElement(arr):
    ans = [None] * len((arr))

    stack = []
    stack.append(0)

    for i in range(1, len(arr)):
        while (len(stack) != 0 and arr[i] > arr[stack[-1]]):
            val = stack.pop()
            ans[val] = arr[i]
        stack.append(i)

    while (len(stack) != 0):
        ans[stack.pop()] = -1
    return ans


# ans = NextGreaterElement([5,9,8,3,2,7,16,4,14,19,3])
# print(ans)

def NextGreaterEkementLeetCode(num1, num2):
    hash = dict()
    stack = []
    stack.append(num2[0])
    count = 0
    for i in range(1, len(num2)):

        while (len(stack) != 0 and (num2[i] > stack[-1])):
            hash[stack.pop()] = num2[i]
        stack.append(num2[i])

    for i in num1:
        if (i in hash):
            print(hash.get(i))
        else:
            print(-1)
    print(hash)


# NextGreaterEkementLeetCode([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7])

def DDII(str):
    stack = []
    count = 1
    for ch in str:
        if(ch=='d'):
            stack.append(count)
            count = count + 1
        else:
            stack.append(count)
            count+=1
            while(len(stack)!=0):
                print(stack.pop())
    while(len(stack)!=0):
        print(stack.pop())



# DDII('dddddddd')

reverseAStringUsingStack("hello")







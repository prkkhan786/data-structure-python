
class Node:
    def __init__(self,data):
            self.data = data
            self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None



    def addLast(self,data):
         newNode = Node(data)
         if(self.head==None):
             self.head = newNode
             newNode.next = None

         else:
             temp = self.head
             while(temp.next is not None):
                 temp = temp.next

             temp.next = newNode
             newNode.next=None

    def addFirst(self,data):

        temp = self.head
        newnode = Node(data)
        if(temp==None):
            self.head = newnode
            newnode.next = None
        else:
            t = self.head
            self.head = newnode
            newnode.next = t


    def Display(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next



li = LinkedList()
li.addLast(10)
li.addLast(20)
li.addFirst(5)
li.Display()






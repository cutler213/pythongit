class node:
    def __init__(self,data):
        self.data=data
        self.next = None

class stack:
    def __init__(self):
        self.head=None

    def push(self,val):
        newnode = node(val)
        newnode.next=self.head
        self.head=newnode

    def pop(self):
        temp=self.head
        print("popped element : ",temp.data)
        self.head = temp.next

    def print_stack(self):
        temp=self.head
        l1=[]
        while temp:
            l1.append(temp.data)
            temp=temp.next
        print(l1)



s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.print_stack()
s1.pop()
s1.print_stack()
s1.pop()
s1.print_stack()


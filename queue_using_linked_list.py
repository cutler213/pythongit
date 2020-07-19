class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,val):
        newnode=node(val)
        if self.front is None and self.rear is None:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode


    def dequeue(self):
        if self.front is None:
            print("no elements in queue")
            return
        self.front=self.front.next
        if self.front is None:
            self.rear=None

    def print_queue(self):
        temp=self.front
        l1=[]
        while temp:
            l1.append(temp.data)
            temp=temp.next
        print(l1)

q1=queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.print_queue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.print_queue()
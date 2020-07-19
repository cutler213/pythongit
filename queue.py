class queue:
    def __init__(self):
        self.items=[]
        self.front=0
        self.rear=0

    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        x=self.front
        self.items.pop(x)
        x=x+1
    def print_queue(self):
        print(self.items)



q1=queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.print_queue()
q1.dequeue()
q1.dequeue()
q1.print_queue()

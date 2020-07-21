class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class hashing:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp:
                temp=temp.next
            temp.next=newnode

size=5




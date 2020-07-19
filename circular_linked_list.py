class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_link_list:
    def __init__(self):
        self.head = None

    def prepend(self,data):
        newnode = node(data)
        if self.head is None:
            newnode.next = newnode
            self.head = newnode
        else:
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
            self.head = newnode

    def display(self):
        temp=[]
        node = self.head
        while node:
            print(node.data)
            node=node.next
            if node==self.head:
                break

    def append(self,data):
        newnode = node(data)
        temp=self.head
        if self.head is None:
            newnode.next = newnode
            self.head = newnode
        else:
            while temp.next!=self.head:
                temp=temp.next
            temp.next = newnode
            newnode.next = self.head

    def search(self,key):
        temp=self.head
        ind=0
        while True:
            if(temp.data==key):
                print(key,"found at",ind)
                return

            temp=temp.next
            ind+=1
            if temp==self.head:
                break
        print("not found")

    def delete(self,key):

        if self.head==None:
            return
        elif self.head.data==key and self.head.next==self.head:
            self.head=None

        elif self.head.data==key:
            last = self.head
            while last.next!=self.head:
                last=last.next
            last.next=self.head.next
            self.head=self.head.next

        else:
            current=self.head
            while current.next!=self.head:
                if current.next.data==key:
                    current.next = current.next.next
                    break

                current=current.next

            






c1 = circular_link_list()
#c1.prepend(10)
#c1.prepend(20)
#c1.prepend(30)
c1.append(10)
c1.append(20)
c1.append(30)
c1.display()
print()
c1.delete(30)
c1.display()


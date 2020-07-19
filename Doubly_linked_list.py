class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Doubly_link_list:
    def __init__(self):
        self.head =None
        self.last = None

    def begin_append(self,data):
        new_node=node(data)
        if self.head is None:
            new_node.prev=None
            new_node.next=None
            self.head = new_node
            return

        new_node.prev=None
        new_node.next=self.head
        self.head.prev = new_node
        self.head = new_node


    def display(self):
        temp=[]
        cur_node = self.head
        while cur_node:
            temp.append(cur_node.data)
            cur_node=cur_node.next
        return temp

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head= new_node
            return
        last_node = self.head
        while last_node.next!=None:
            last_node=last_node.next
        last_node.next=new_node
        new_node.prev = last_node
        new_node.next=None

    def rev_trav(self):
        cur=self.head
        temp=[]
        while cur.next!=None:
            cur=cur.next

        while cur!=self.head:
            temp.append(cur.data)
            cur=cur.prev
        temp.append(cur.data)
        return temp

    def delete_node(self,key):
        if self.head==None:
            return
        temp=self.head
        while temp!=None and temp.data!=key:
            temp=temp.next
        if temp==None:
            print("key not found")
            return
        elif temp==self.head:
            self.head=temp.next
            self.head.prev=None
        elif temp.next==None:
            temp.prev.next = None

        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev





d1= Doubly_link_list()
#d1.begin_append(10)
#d1.begin_append(20)
#d1.begin_append(30)
d1.append(10)
d1.append(20)
d1.append(30)
d1.append(40)
d1.append(50)
print(d1.display())
#print(d1.rev_trav())
d1.delete_node(30)
print(d1.display())





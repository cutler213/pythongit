class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node=cur_node.next
        cur_node.next=new_node
    def begin_add(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after(self,idx,new_data):
        cnt=0
        new_node = node(new_data)
        cur_node =self.head
        while True:

            if cnt==idx:
                new_node.next = cur_node.next
                cur_node.next = new_node
                break
            cnt+=1
            cur_node = cur_node.next


    def length(self):
        idx=0
        cur_node = self.head
        while cur_node:
            idx+=1
            cur_node = cur_node.next
        return idx

    def dispay(self):
        temp = []

        cur_node = self.head
        while cur_node:

            temp.append(cur_node.data)
            cur_node=cur_node.next

        print(temp)
    def get(self,idx):
        if idx>=self.length():
            print("error in get: index out of bound")
        cur_node = self.head
        ind=0
        while True:

            if ind==idx:
                return cur_node.data
            else:
                ind+=1
                cur_node = cur_node.next
    def erase(self,idx):
        if idx>=self.length():
            print("error in erase: index out of bound")
        cur_node = self.head
        ind=0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if ind == idx:
                last_node.next=cur_node.next
                return
            else:
                ind+=1
    def get_middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                slow_ptr=slow_ptr.next
                fast_ptr=fast_ptr.next.next
            return slow_ptr.data

    def rev_iterative(self):
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev

    def rev_recursive(self):
        def helper_rec(cur,prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return helper_rec(cur,prev)
        self.head = helper_rec(cur=self.head,prev=None)

    def print_last_n(self,n):
        cur=self.head
        len=0
        while cur:
            cur=cur.next
            len+=1
        temp=self.head
        for i in range(len-n):
            temp=temp.next
        print(temp.data)
    def detect_loop(self):
        s=list()
        cur=self.head
        while cur:
            if cur in s:
                return True
            s.append(cur)
            cur=cur.next
        return False

    def detect_loop_2_ptr(self):
        slow = self.head
        fast = self.head
        while slow!=None and fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print("loop is here")
                break



        













l1 = linked_list()
#l1.head=node(0)
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
#print(l1.length())
print ('Created linked list is:')
#l1.dispay()
#l1.insert_after(0,6)
#l1.dispay()
#print(l1.get(1))
l1.dispay()
#l1.rev_iterative()
#l1.rev_recursive()
#l1.print_last_n(5)
#print(l1.get_middle_node())
#print("print data at 2 index is:%d" % l1.get(2))
#l1.erase(1)
#print(l1.dispay())
l1.head.next.next.next.next.next = l1.head
#print(l1.detect_loop())
l1.detect_loop_2_ptr()
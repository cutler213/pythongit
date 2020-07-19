class heap:
    def __init__(self):
        self.heap=[]

    def get_parent(self,i):
        return int((i-1)/2)

    def get_left_child(self,i):
        return 2*i+1

    def get_right_child(self,i):
        return 2*i+2

    def has_parent(self,i):
        return self.get_parent(i)>=0
    def has_left(self,i):
        return self.get_left_child(i)<len(self.heap)
    def has_right(self,i):
        return self.get_right_child(i)<len(self.heap)
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def insert(self,key):
        self.heap.append(key)
        self.heapify(len(self.heap)-1)

    def heapify(self,i):
        while self.has_parent(i) and self.heap[i]>self.heap[self.get_parent(i)]:
            self.swap(i,self.get_parent(i))
            i=self.get_parent(i)

    def print_heap(self):
        print(self.heap)

    def delete_node(self,i):
        last=len(self.heap)-1
        self.swap(i,last)
        self.heap.pop()
        for i in range(len(self.heap)-1):
            self.heapify(i)


h1=heap()
h1.insert(10)
h1.insert(20)
h1.insert(40)
h1.insert(30)
h1.insert(80)
h1.insert(60)
h1.insert(50)
h1.print_heap()
h1.delete_node(0)
h1.print_heap()

"""
arr=[10,20,40,30,80,60,50]
[10, 80, 60, 30, 20, 40, 50]
size=len(arr)-1
#print(size)
mid=int(size/2)

def buildheap(arr,size):
    for i in range(mid,0,-1):
        heapify(arr,i,size)


def heapify(arr,i,size):
    left=2*i+1
    right=left+1
    max=i

    if left<=size and arr[left]>arr[max]:
        max=left

    if right<=size and arr[right]>arr[max]:
        max=right

    if i!=max:
        arr[max],arr[i]=arr[i],arr[max]


buildheap(arr,size)
print(arr)
"""
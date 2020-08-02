def biuld_heap(arr,size):
    for i in range(size//2-1,-1,-1):
        heapify(arr,size,i)
    print(num)
    for i in range(size-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

def heapify(arr,n,i):
    max=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[max]<arr[left]:
        max=left
    if right<n and arr[max]<arr[right]:
        max=right

    if max!=i:
        arr[i],arr[max]=arr[max],arr[i]
        heapify(arr,n,max)


num=[10,20,30,40,50,60,80]
print(num)
sz=len(num)
biuld_heap(num,sz)
print(num)
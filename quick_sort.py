def partition(arr,st,end):
    pindex=st
    pivot=arr[end]
    for i in range(st,end):
        if arr[i]<pivot:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[end],arr[pindex]=arr[pindex],arr[end]
    return pindex


def quicksort(arr,st,end):
    if st<end:
        pindex=partition(arr,st,end)
        quicksort(arr,st,pindex-1)
        quicksort(arr, pindex+1, end)

l1=[10,3,50,25,20]
print(l1)

quicksort(l1,0,len(l1)-1)
print(l1)
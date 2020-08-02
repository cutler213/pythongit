def merge_sort(l1,l2):
    i=0
    j=0
    l3=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1

    while i<len(l1):
        l3.append(l1[i])
        i+=1
    while j<len(l2):
        l3.append(l2[j])
        j+=1



def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l1=arr[:mid]
        l2=arr[mid:]
        merge(l1)
        merge(l2)
        i = 0
        j = 0
        k=0

        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                arr[k]=l1[i]
                i += 1
            else:
                arr[k] = l2[j]
                j += 1
            k+=1

        while i < len(l1):
            arr[k]=l1[i]
            i += 1
            k+=1
        while j < len(l2):
            arr[k]=l2[j]
            j += 1
            k+=1



l4=[55,52,56,18,1,3]
print(l4)
merge(l4)
print(l4)
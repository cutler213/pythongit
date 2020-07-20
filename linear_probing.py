arr = [-1, -1, -1, -1, -1]

def insert(data):
    global arr
    size=len(arr)
    key=data%size
    index=key
    while arr[index]!=-1:
        index=(index+1)%size
        if key==index:
            print("travesersed hash fully, no space left")
            break
    arr[index]=data

def delete(data):
    global arr
    size=len(arr)
    key=data%size
    index=key
    while arr[index]!=data:
        index=(index+1)%size
        if key==index:
            print(data,"is not present")
            return 0
    arr[index]=-1

def quadratic_probing(data):
    global arr
    size = len(arr)
    key = data % size
    index = key
    i=1
    if -1 in arr:
        while arr[index]!=-1:
            index=(index+pow(i,2))%size
            i+=1
        arr[index]=data



print(arr)
quadratic_probing(10)
quadratic_probing(15)
quadratic_probing(2)
quadratic_probing(5)
quadratic_probing(4)
quadratic_probing(43)
#insert(10)
#insert(15)
#insert(2)
#insert(5)
#insert(4)
#insert(20)
print(arr)
#delete(20)
print(arr)



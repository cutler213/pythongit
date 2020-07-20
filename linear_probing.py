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

print(arr)
insert(10)
insert(15)
insert(2)
insert(4)
insert(5)
insert(20)
print(arr)



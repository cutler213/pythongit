def search(arr,st,end,key):
    if st<=end:
        mid=(st+end)//2
        if arr[mid]==key:
            print(key,"found")
        elif key<arr[mid]:
            search(arr,st,mid-1,key)
        else:
            search(arr,mid+1,end,key)
    else:
        print("not present")

def search_it(arr,st,end,key):

    while st<=end:
        mid=(st+end)//2
        if arr[mid]==key:
            print("found")
            return
        elif arr[mid]<key:
            st=mid+1
        else:
            end=mid-1


l1=[1,2,3,4,5,6,7]
search_it(l1,0,len(l1)-1,2)
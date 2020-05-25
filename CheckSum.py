def checksum(arr,sum):
    l=0
    r=len(arr)
    new=arr
    for i in range(0,r):
        for j in range(i+1,r):
            if new[i] + new[j] == sum:
                print(str(new[i]),' ',str(new[j]),' gives ',sum)

def arprint(sa):
    l=len(sa)
    print(l)
    for i in sa:
        print (i)




num = [-8, 1, 4, 6, 10, 45]
num2 = [10,6,3,13,12,4]


#arprint(num)
#checksum(num2,16)
print (''.join(reversed('turbo')))
s='dad'
print(s[::-1])

def rev_slice(d):
    print(d[::-1])

def rev_join(d):
    print(''.join(reversed(d)))




import timeit
#str='abcdefghijklmnopqrstuvwxyz'


def checksum_f(arr,sum):
    l=0
    r=len(arr)-1
    new=sorted(arr)
    while l<len(arr):
        if new[l] > new[r] :
            break
        elif new[l] + new[r] == sum :
            print(str(new[l]),' ',str(new[r]),' gives ',str(sum))
            l+=1

        elif  new[l] + new[r] < sum :
            l+=1
        elif new[l] + new[r] > sum :
            r-=1


checksum_f(num2,16)
3,4,6,10,12,13

def getpairs(arr,sum):
    m = [0]*1000
    n=len(arr)
    twice_count=0
    for i in range(0,n):
        m[arr[i]]
        m[arr[i]] += 1
        twice_count += m[sum - arr[i]]
        if (sum - arr[i] == arr[i]):
            twice_count -= 1
    print(twice_count)

#getpairs(num2,16)

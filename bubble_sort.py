import time

def bsort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums=[5,3,8,7,6,2]

t0=time.time()

bsort(nums)
t1=time.time()
print(nums)

print("time taken", t1-t0)
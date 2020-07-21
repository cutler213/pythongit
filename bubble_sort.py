import time

def bsort(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

def bsortmax(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j]<nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]


nums=[5,3,8,7,6,2]

t0=time.time()

bsortmax(nums)
t1=time.time()
print(nums)

print("time taken", t1-t0)
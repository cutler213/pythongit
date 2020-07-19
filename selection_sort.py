def sort(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,len(nums)):

            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp

###############################
def sortmax(nums):
    for i in range(len(nums)-1,0,-1):
        maxpos=i
        for j in range(i):

            if nums[j]>nums[maxpos]:
                maxpos=j
        temp=nums[i]
        nums[i]=nums[maxpos]
        nums[maxpos]=temp

nums=[5,3,8,6,7,2]

print(nums)
sortmax(nums)

print(nums)
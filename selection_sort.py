def sort(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,len(nums)):

            if nums[j]<nums[minpos]:
                nums[j],nums[minpos]=nums[minpos],nums[j]


###############################
def sortmax(nums):
    for i in range(len(nums)-1,-1,-1):
        maxpos=i
        for j in range(i,-1,-1):

            if nums[j]<nums[maxpos]:
                nums[j], nums[maxpos] = nums[maxpos], nums[j]


nums=[5,3,8,6,7,2]

print(nums)
sortmax(nums)

print(nums)
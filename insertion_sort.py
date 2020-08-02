def insertion(nums):
    for i in range(1,len(nums)):
        val=nums[i]
        index=i
        while index>0 and nums[index-1]>val:
            nums[index]=nums[index-1]
            index-=1
        nums[index]=val



nums=[6,7,8,9,1]
print(nums)
insertion(nums)
print(nums)



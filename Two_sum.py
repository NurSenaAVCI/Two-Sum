# Given an array of integers  and an integer , return indices of the two numbers such that they add up to target.numstarget

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])

nums = [2,7,11,15]
target = 9
for a in nums:
    for k in nums:
        if a+k == target and a<k:
            print([a,k])


# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? Find all unique triplets in the array which gives 
# the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]



def threeSum(nums):

    nums.sort()
    result = []

    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i-1]:
            continue
        
        left=i+1
        right=len(nums)-1
        
        while left<right:
            total =nums[i]+nums[left]+nums[right]
            # print(total)

            if total < 0:
                left=left+1
            elif total> 0:
                right=right-1
            else:
                result.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left] == nums[left+1]:
                    left= left+1
                while left < right and nums[right] == nums[right-1]:
                    right=right-1

                left=left+1
                right=right-1
    # print(result)
    return result

nums = [-1, 0, 1, 2, -1, -4]
nums2= [-1,-2,-4,0,-6,-7,8,-9,12,-12,-3,3,4,5,10,-19,2,3,4,5,6,7,8,-10,10,11,]

print(len(threeSum(nums)))
print(threeSum(nums))
print(len(threeSum(nums2)))
print(threeSum(nums2))
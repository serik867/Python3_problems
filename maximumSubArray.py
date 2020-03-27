# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle.

def maxSubArray(nums) -> int:
    
    for i in range(1, len(nums)):
        largestSum = max(nums[i], nums[i-1] + nums[i])
        nums[i] = largestSum

    return max(nums)


test_cases = [[-2,1,-3,4,-1,2,1,-5,4],
            [1,2,-1,3,-4,4,5,-4,-7,4,8,7,9,-4],
            [2,6,3,6,7,-2,-3,4,5,6,-6,-3]]

for i in test_cases:
    print(maxSubArray(i))




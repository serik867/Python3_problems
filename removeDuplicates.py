# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.


def removeDuplicates(nums) -> int:
    i=0
    while i < len(nums)-1:
        if nums[i+1] == nums[i]:
            nums.remove(nums[i])
        else:
            i+=1
    print(nums)
    return len(nums)


    # nums[:] = list(set(nums))
    # nums.sort()
    # return len(nums)
        
test_case = [[0,0,1,1,1,2,2,3,3,4],[1,1,2], [1,1,1,1,2,2,2,2,3,3,3,4,4,5,6,7]]

for i in test_case:
    print( removeDuplicates(i))

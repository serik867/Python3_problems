# Given n non-negative integers a1, a2, ..., an , 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) 
# and (i, 0). Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.
# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

def max_Area(height) -> int:
    point1=0
    point2=len(height)-1
    maxArea=0

    while point1 != point2:
        if (point2 - point1) * min(height[point1],height[point2]) > maxArea:
            maxArea = (point2 - point1) * min(height[point1],height[point2])
        elif height[point1] == min(height[point1],height[point2]):
            point1+=1
        else:
            point2-=1
    
    return maxArea

test_cases = [[1,8,6,2,5,4,8,3,7], [2,3,5,7,6,8,9,7,9],[9,3,7,9,1,2,8,5],[2,3,5,6,8,9,4,3,2,4,6]]


for i in range(len(test_cases)):
    print( "Test Case - "+ str(i))
    print(max_Area(test_cases[i]))
# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

def reverseString( s) -> None:

    left=0
    rigth=len(s)-1
    
    while left < rigth:
        temp = s[left]
        s[left] = s[rigth]
        s[rigth]= temp
        
        left+=1
        rigth-=1
    
    return s

test_case = ["S","e","r","d","a","r"]

print(reverseString(test_case))
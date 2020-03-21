# Given a string and an integer k, you need to reverse the first k characters 
# for every 2k characters counting from the start of the string. If there are 
# less than k characters left, reverse all of them. If there are less than 2k but 
# greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

def reverseStr(s: str, k: int) -> str:
        
    letters= list(s)
    
    for i in range(0,len(letters),2*k):
        letters[i:i+k] = letters[i:i+k][::-1]
    
    return "".join(letters)

test_cases = ["abcdefgh", "serdar", "blablablabla", "honey", "hahahahahaha"]

for i in range(len(test_cases)):
    print(reverseStr(test_cases[i],2))


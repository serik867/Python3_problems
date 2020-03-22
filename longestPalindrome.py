# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"




def longestPalindrome(s: str) -> str:
    
    word=""
    
    
    if len(s) == 1:
        return s
    
    for i in range(len(s)-1):
        for j in range(i+1,len(s)+1):
            
            s1=s[i:j]
            
            if s1 == s1[::-1]:
                if len(word) < len(s1):
                    word=s1
    
    return word
    
test_cases=["cc","aaa","babab","babasb", "adadadda", "c"]

for i in range(len(test_cases)):

    print(longestPalindrome(test_cases[i]))
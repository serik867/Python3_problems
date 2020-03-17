# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

def longestCommonPrefix(strs):
    #### Solution 1

    # if len(strs) == 0:
    #     return ""
    
    # ans = []
    # i = 0
    # size = min([len(x) for x in strs])

    # while i < size:
    #     if len(set([x[i] for x in strs])) == 1:
    #         ans.append(strs[0][i])
    #     else:
    #         break
    #     i+=1
    # return "".join(ans)
    
    ##### Solution 2

    if len(strs) == 0:
        return ""

    word=strs[0]
    for i in range(1,len(strs)):
        j=0
        check=True
        while check:
            if j < min([len(word),len(strs[i])]) and word[j]==strs[i][j]:
                j+=1
            else:
                word=word[:j]
                check=False
    return word


test_cases=["flower","flow","flight"]
print(longestCommonPrefix(test_cases))  
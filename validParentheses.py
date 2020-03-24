def isValid(s: str) -> bool:
#  Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
    
    i=0
    n=(len(s)//2)+1
    while(i<n):
        s=s.replace("()","")
        s=s.replace("{}","")
        s=s.replace("[]","")
        i+=1
    return len(s)==0

test_cases= "{}[]"
test_cases1="{({[]})}"
test_cases2="{}({])"

print(isValid(test_cases))
print(isValid(test_cases1))
print(isValid(test_cases2))
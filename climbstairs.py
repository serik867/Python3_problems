def climbStairs( n: int) -> int:
    if n<2:
        return 1
    
    dp= list()
    dp.insert(0,1)
    dp.insert(1,1)
    
    for i in range(2,n+1):
        dp.insert(i, dp[i-1]+dp[i-2])
    
    return dp[n]

test_case=[1,2,3,4,5,6,7,8,9]

for i in test_case:
    print(climbStairs(i))
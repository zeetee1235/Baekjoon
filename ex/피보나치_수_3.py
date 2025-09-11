n = int(input())
mod = 1000000
# 피사노 주기 10^k 일때 (k > 2) 15 * 10 ^(k - 1)
period = 1500000

def fibonacci(m):
    if m == 0:
        return [0]
    dp = [0] * (m + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, m + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    return dp

arr = fibonacci(period)
print(arr[n % period])


    
    


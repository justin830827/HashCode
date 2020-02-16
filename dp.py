def solve_pizza(nums, target):
    dp = [[None for _ in range(len(nums))] for _ in range(target+1)]

    dp[nums[0]][0] = [0]

    for j in range(len(nums)):
        dp[0][j] = []

    for i in range(target+1):
        for j in range(len(nums)):
            if j-1 >= 0:
                if dp[i][j-1] is not None:
                    dp[i][j] = dp[i][j-1]
                    continue
                if i-nums[j] >= 0:
                    if dp[i-nums[j]][j-1] is not None:
                        dp[i][j] = list(dp[i-nums[j]][j-1] + [j])
    
    for i in range(target, -1, -1):
        if dp[i][-1] is not None:
            return dp[i][-1]
    
if __name__ == '__main__':
    solve_pizza([2, 5, 6, 8], 17)
    
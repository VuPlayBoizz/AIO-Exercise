def levenshtein_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        dp[i][0] = i
    for j in range(n):
        dp[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j],        
                               dp[i][j - 1],       
                               dp[i - 1][j - 1]) + 1  

    
    return dp[m - 1][n - 1]

if __name__ == "__main__":
    s = "yu"
    t = "you"
    result = levenshtein_distance(s, t)
    print(f"Khoảng cách Levenshtein giữa '{s}' và '{t}' là: {result}")

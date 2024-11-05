def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[""] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                print(f"str1 = {str1[i-1]}, str2={str2[j - 1]} ")
                print(f"loop i = {i} m={m} n={n}, loop j={j}, dp= {dp[i][j]}\n")
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
                print(f"str1 = {str1[i - 1]}, str2={str2[j - 1]} ")
                print(f"loop i = {i} m={m} n={n}, loop j={j}, dp= {dp[i][j]}\n")
        print(f"loop i = {i} n={n}, loop j={j}, dp= {dp[m][n]}\n")

    # The LCS will be in the bottom-right cell
    return dp[m][n]

# Test the function with the example input
str1 = "KEPETAHAN"
str2 = "PERCAKAPAN"
print("Expected output:", longest_common_subsequence(str1, str2))  # Should print "MJAU"

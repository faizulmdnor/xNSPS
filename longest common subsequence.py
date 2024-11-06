def longest_common_subsequence(str1, str2):
    # Get the lengths of the two strings
    m, n = len(str1), len(str2)

    # Initialize a 2D list (dp table) where each cell dp[i][j] stores the LCS of str1[:i] and str2[:j]
    # The table has (m + 1) rows and (n + 1) columns, initially filled with empty strings
    dp = [[""] * (n + 1) for _ in range(m + 1)]

    # Loop through each character in str1, with 'i' indicating the current index in str1 (1-based)
    for i in range(1, m + 1):
        # For each character in str1, loop through each character in str2
        for j in range(1, n + 1):
            # Check if the current characters of str1 and str2 match
            if str1[i - 1] == str2[j - 1]:  # str1[i-1] and str2[j-1] are the actual characters at index i-1 and j-1
                # If they match, extend the LCS by adding this character to the result in dp[i-1][j-1]
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                print(dp)

                # Print debugging information about the matching characters and updated dp value
                print(f"str1 = {str1[i - 1]}, str2 = {str2[j - 1]} ")
                print(f"loop i = {i}, m = {m}, n = {n}, loop j = {j}, dp = {dp[i][j]}\n")
            else:
                # If they do not match, carry forward the longest LCS found so far from dp[i-1][j] or dp[i][j-1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

                # Print debugging information about non-matching characters and current dp value
                print(f"str1 = {str1[i - 1]}, str2 = {str2[j - 1]} ")
                print(f"loop i = {i}, m = {m}, n = {n}, loop j = {j}, dp = {dp[i][j]}\n")

        # Print the current LCS for each row iteration in str1 to show progress
        print(f"After loop i = {i}, current LCS length = {len(dp[i][n])}, dp[i][n] = {dp[i][n]}\n")

    # The final longest common subsequence for str1 and str2 is in the bottom-right cell of dp table, dp[m][n]
    return dp[m][n]

# Test the function with an example input
str1 = "AMDOIED"
str2 = "DEIODM"

# Expected output is the LCS, which is the longest subsequence present in both str1 and str2
print("Expected output: ", longest_common_subsequence(str1, str2))

"""
Explanation of Key Sections:
Input Lengths: m and n store the lengths of str1 and str2 to help with loop bounds.

DP Table Initialization: dp is a 2D table filled with empty strings. Each dp[i][j] will hold the LCS for substrings str1[:i] and str2[:j].

Nested Loops:

Outer Loop (over str1): i goes from 1 to m, iterating through each character in str1.
Inner Loop (over str2): j goes from 1 to n, iterating through each character in str2.
Character Match Check: If characters at str1[i - 1] and str2[j - 1] match, extend the previous LCS by adding the character to dp[i][j].
No Match: If characters don't match, take the longer subsequence from dp[i-1][j] or dp[i][j-1].
Debugging Statements: The print statements help show:

Matching and non-matching characters at each step.
So far, the LCS has built up in dp[i][j].
Final LCS: The cell dp[m][n] holds the LCS for the entire str1 and str2.

This code will display step-by-step details of how the LCS is constructed and output the final LCS for the given example input strings.
"""

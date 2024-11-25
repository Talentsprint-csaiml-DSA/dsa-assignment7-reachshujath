def longest_common_subsequence(str1, str2):
    # maxlen = {(i,j) : 0 for i in range(len(str1) + 1) for j in range(len(str2)+1)}
    maxlen = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1)+1)]
    print(maxlen)
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # Build the result array from bottom up with the following logic
            # If there is a match then add 1 to the value of maxlen[i-1][j-1]
            # If there is a mismatch then choose the maximum of maxlen[i-1][j]
            # and maxlen[i][j-1]
            if str1[i-1] == str2[j-1]:
                maxlen[i][j] = 1 + maxlen[i-1][j-1]
            else:
                maxlen[i][j] = max(maxlen[i-1][j], maxlen[i][j-1])
    return maxlen[i][j]
               

# print(longest_common_subsequence("abdc", "abfecd"))
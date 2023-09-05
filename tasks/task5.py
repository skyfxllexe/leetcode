def longestPalindrome(s):
    maxim = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > maxim:
                maxim = max(maxim, len(s[i:j]))
                maximS = s[i:j]
    return maximS
print(longestPalindrome(''))
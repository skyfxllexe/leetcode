def firstUniqChar(s):
    myDict = dict()
    for i in s:
        if i not in myDict.keys():
            myDict[i] = 0
        myDict[i] += 1
    for i in range(len(s)):
        if myDict[s[i]] == 1:
            return i
    return -1
print(firstUniqChar("aabb"))
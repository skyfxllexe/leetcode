def findDuplicate(nums):
    myDict = dict()
    for i in nums:
        if i in myDict:
            return i
        if i not in myDict:
            myDict[i] = 1

findDuplicate([1,3,3,4,2,2])
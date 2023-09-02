def findTheDifference(s, t):
    dict1 = dict()
    dict2 = dict()
    for i in s:
        if i not in dict1.keys():
            dict1[i] = 0
        dict1[i] += 1
    for i in t:
        if i not in dict1.keys():
            dict2[i] = 0
        dict2[i] += 1
    for i in dict2.keys():
        if i not in dict1:
            
            dict1[i] != dict2[i]
    
print(findTheDifference("ae", "aea"))
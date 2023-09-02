def canConstruct(ransomNote, magazine):
    dict1 = dict()
    dict2 = dict()
    for i in magazine:
        if i not in dict1.keys():
            dict1[i] = 0
        dict1[i] += 1
    for i in ransomNote:
        if i not in dict2.keys():
            dict2[i] = 0
        dict2[i] += 1
    for i in dict2.keys():
        if i in dict1.keys():
            if dict1[i] < dict2[i]:
                return False
        else:
            return False
    return True
print(canConstruct('bg','efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'))
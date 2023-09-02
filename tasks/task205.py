def isIsomorphic(s, t):
    dict1 = dict()
    dict2 = dict()
    if len(set(s)) != len(set(t)):
        return False
    for i in range(len(s)):
        if s[i] not in dict1.keys():
            dict1[s[i]] = [i+1]
        else:
            dict1[s[i]].append(i+1)
    for i in range(len(t)):
        if t[i] not in dict2.keys():
            dict2[t[i]] = [i+1]
        else:
            dict2[t[i]].append(i+1)
    return list(dict1.values()) == list(dict2.values())
print(isIsomorphic("abab", "baba"))
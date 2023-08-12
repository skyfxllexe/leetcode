def isSubsequence(s: str, t: str) -> bool:
    if s == '':
        return True
    counter = 0
    answer = ''
    for i in range(len(t)):
        if t[i] == s[counter]:
            answer += t[i]
            counter += 1*(counter+1<len(s))
    return answer == s
print(isSubsequence('b', 'abc'))
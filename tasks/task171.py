def titleToNumber(columnTitle: str):
    alphabet = sorted(set('qwertyuiopasdfghjklzxcvbnm'))
    myDict = dict()
    for i in range(len(alphabet)):
        myDict[alphabet[i].lower()] = i
    answer = 0
    degree = len(columnTitle)-1
    for i in columnTitle.lower():
        answer += 26**degree * (myDict[i]+1)
        degree -= 1
    if len(columnTitle) == 1:
        return myDict[columnTitle.lower()]+1
    return answer

print(titleToNumber("Z"))
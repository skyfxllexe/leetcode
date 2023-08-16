def reverseWords(s: str) -> str:
    s = s.split(' ')
    new_s = []
    for i in s:
        if i != '':
            new_s.append(i)
    return ' '.join(new_s[::-1])
print(reverseWords('zero as one'))
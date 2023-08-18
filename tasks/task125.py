def isPalindrome(s):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    answer = ''
    for i in s:
        if i.lower() in alphabet:
            answer += i.lower()
    return answer
print(isPalindrome("0P"))
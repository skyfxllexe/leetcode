def countBits(n):
    ans = []
    for i in range(n+1):
        counter = 0
        temp = i
        while temp > 0:
            counter += temp%2
            temp //= 2
        ans.append(counter)
    return ans
print(countBits(5))
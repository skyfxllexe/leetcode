def reverse(x: int) -> int:
        string = str(x)
        flag = string[0] == '-'
        string = string[1*flag:]
        return int(string[::-1])*(abs(int(string[::-1])) < 2**31)*(-1)**flag


def romanToInt(s: str) -> int:
    num = 0
    x=0
    # for x in range(0,len(s)):
    while x < len(s):
        if s[x] == 'M':
            num +=1000
        elif s[x] == 'D':
            num += 500
        elif s[x] == 'C':
            if x+1 < len(s):
                if s[x+1] == 'M':
                    num +=900
                    x += 1
                elif s[x+1] == 'D':
                    num += 400
                    x += 1
                else: 
                    num += 100
            else: num += 100
        elif s[x] == 'L':
            num += 50
        elif s[x] == 'X':
            if x+1 < len(s):
                if s[x+1] == 'C':
                    num +=90
                    x += 1
                elif s[x+1] == 'L':
                    num += 40
                    x += 1
                else:
                    num += 10
            else:
                num += 10
        elif s[x] == 'V':
            num += 5
        else:
            if x+1 < len(s):
                if s[x+1] == 'X':
                    num +=9
                    x += 1
                elif s[x+1] == 'V':
                    num += 4
                    x += 1
                else:
                    num += 1
            else:
                num += 1
        x +=1
    return num


# print(romanToInt('III'))
print(romanToInt('XLV'))
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
        longest = 0
        overall = 0
        for x in range(0,len(strs)-1):
            if strs[x] == strs[x+1]:
                longest= x
            else:
                for y in range (0,len(x)):
                    if strs[x][y] == str[x+1][y]:
                        longest = x
                    else:
                        break
            if longest < overall and overall > 0:
                    overall = longest
            elif overall == 0 and longest > 0:
                 overall = longest
        
        return strs[:overall]


timmy=['flower','flower']
print(longestCommonPrefix(timmy))
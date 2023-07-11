from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    overall = -1
    if len(strs) == 1:
            overall = len(strs[0])
    else:
        for x in range(0,len(strs)-1):
            longest = 0
            if strs[x] == strs[x+1]:
                longest= len(strs[x])
            else:
                shortest = len(strs[x])
                if len(strs[x+1]) < shortest:
                    shortest = len(strs[x+1])
                for y in range (0,shortest):
                    if strs[x][y] == strs[x+1][y]:
                        longest += 1
                    else:
                        break
            if longest < overall and overall > -1:
                    overall = longest
            elif overall == -1:
                overall = longest
    if overall == -1:
        overall = 0
    return strs[0][:overall]


print(longestCommonPrefix(['fl','flower','flower']))
print(longestCommonPrefix(['a']))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["reflower","flow","flight"]))